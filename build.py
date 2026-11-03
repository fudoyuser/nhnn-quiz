#!/usr/bin/env python3
"""Ghép src/ + data/*.json thành index.html (GitHub Pages).

Dùng: python3 build.py [đường_dẫn_bản_artifact.html]
Tham số tùy chọn ghi thêm một bản không có khung <html>/<head> để xuất bản dạng Artifact.
"""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).parent
ORDER = ["vbhn117", "vbhn118"]          # thứ tự hiển thị trong thư viện
TYPES = {"nho", "so", "ss", "th", "nd", "order", "match", "pb"}


def check(doc):
    errs = []
    for i, q in enumerate(doc["qs"]):
        tag = f'{doc["id"]}#{i}'
        k = q.get("k", "mcq")
        if q.get("ch") not in doc["chapters"]:
            errs.append(f"{tag}: chương {q.get('ch')} không có")
        if q.get("ty", "nho") not in TYPES:
            errs.append(f"{tag}: dạng {q.get('ty')} không hợp lệ")
        for f in ("q", "c", "ex"):
            if not q.get(f):
                errs.append(f"{tag}: thiếu {f}")
        if k == "mcq":
            o = q.get("o", [])
            if len(o) != 4 or len(set(o)) != 4:
                errs.append(f"{tag}: cần 4 phương án khác nhau")
        elif k == "order":
            if len(q.get("items", [])) < 3:
                errs.append(f"{tag}: câu sắp xếp cần ít nhất 3 bước")
        elif k == "match":
            p = q.get("pairs", [])
            if len(p) < 3 or len({r for _, r in p}) != len(p):
                errs.append(f"{tag}: câu nối cặp cần ít nhất 3 cặp, vế phải không trùng")
        else:
            errs.append(f"{tag}: loại {k} không hợp lệ")
    return errs


def main():
    docs = [json.loads((ROOT / "data" / f"{d}.json").read_text("utf-8")) for d in ORDER]
    errs = [e for d in docs for e in check(d)]
    if errs:
        sys.exit("Lỗi dữ liệu:\n" + "\n".join(errs))
    data = json.dumps(docs, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    js = (ROOT / "src/app.js").read_text("utf-8").replace("/*DATA*/[]", data, 1)
    head = (ROOT / "src/head.html").read_text("utf-8")
    body = (ROOT / "src/body.html").read_text("utf-8")
    page = f"{head}\n{body}\n<script>\n{js}</script>\n"
    shell = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
             '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
             '<meta name="description" content="Quiz trắc nghiệm và phản biện văn bản pháp luật của Ngân hàng Nhà nước Việt Nam, mỗi đáp án kèm trích dẫn điều khoản.">\n'
             '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n')
    full = shell + page.replace("</style>\n\n<div class=\"wrap\">", "</style>\n</head>\n<body>\n<div class=\"wrap\">", 1) + "</body>\n</html>\n"
    (ROOT / "index.html").write_text(full, "utf-8")
    if len(sys.argv) > 1:
        pathlib.Path(sys.argv[1]).write_text(page, "utf-8")
    for d in docs:
        ty = {}
        for q in d["qs"]:
            ty[q.get("ty", "nho")] = ty.get(q.get("ty", "nho"), 0) + 1
        longest = sum(1 for q in d["qs"] if q.get("k", "mcq") == "mcq"
                      and len(q["o"][0]) == max(len(x) for x in q["o"]))
        mcq = sum(1 for q in d["qs"] if q.get("k", "mcq") == "mcq")
        print(f'{d["no"]}: {len(d["qs"])} câu {ty} · đáp án dài nhất {longest}/{mcq}')


if __name__ == "__main__":
    main()
