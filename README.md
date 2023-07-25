# pdf_to_txt

PDF を txt ファイルに変換するコード. このコードを使うことで, [Code Interpreter](https://beta.openai.com/docs/introduction/code-interpreter) で PDF を読ませるときに前処理の不確実性を減らすことができる.

## 使い方

```bash
python watch.py
```

を実行している間は, `./pdf` ディレクトリに PDF ファイルを置くと, `./txt` ディレクトリに txt ファイルが生成される.

手動で変換したい場合は,

```bash
convert.py <pdf_path>
```

を実行する.
