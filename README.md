# number-yomiage（すうじよみあげ100）

1〜100の数字盤。タップすると数字を読み上げる子ども向けWebページ。

- 日本語：VOICEVOXで録音した音声（`ja_f/` 春日部つむぎ、`ja_m/` 玄野武宏）
- 英語：端末の読み上げ音声（Web Speech API）
- かけながし：「つづけて よむ」ON でタップした数字から100まで、「▶ 1から」「▶ 10ずつ」

## 音声の作り直し

VOICEVOX一式を `/root/vv/` に入れてから、リポジトリ直下で `python3 scripts/gen_voices.py`。

## クレジット

VOICEVOX:春日部つむぎ / VOICEVOX:玄野武宏（一般公開時は各キャラクターの利用規約を確認）
