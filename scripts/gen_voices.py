"""すうじよみあげ100の日本語音声（1〜100 × 女性・男性）を作り直すスクリプト。
VOICEVOX一式を /root/vv/ に入れてから、リポジトリ直下で実行する。"""
import subprocess
from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile
V="/root/vv/"
ort=Onnxruntime.load_once(filename=V+"voicevox_onnxruntime-linux-x64-1.23.2/lib/libvoicevox_onnxruntime.so.1.23.2")
syn=Synthesizer(ort,OpenJtalk(V+"open_jtalk_dic_utf_8-1.11"))
for f in ("0","4"):
    with VoiceModelFile.open(V+f"vvms/{f}.vvm") as m: syn.load_voice_model(m)
ONES=["","イチ","ニ","サン","ヨン","ゴ","ロク","ナナ","ハチ","キュウ"]
TENS=["","ジュウ","ニジュウ","サンジュウ","ヨンジュウ","ゴジュウ","ロクジュウ","ナナジュウ","ハチジュウ","キュウジュウ"]
def y(n): return "ヒャク" if n==100 else TENS[n//10]+ONES[n%10]
for d,sid in (("ja_f",8),("ja_m",11)):
    for n in range(1,101):
        q=syn.create_audio_query(y(n),sid)
        q.speed_scale=0.95; q.pre_phoneme_length=0.05; q.post_phoneme_length=0.1
        open("/tmp/t.wav","wb").write(syn.synthesis(q,sid))
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/t.wav","-ac","1","-b:a","64k",f"{d}/{n}.mp3"],check=True)
