data = [
    {
        "Category": "\u53bb\u75f0\u85ac",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a1\u56de10\u338e/\u338f\u30001\u65e53\u56de\u307e\u3067",
        "Name": "\u30e0\u30b3\u30c0\u30a4\u30f3DS50%",
        "Taste": "\u30d4\u30fc\u30c1"
    },
    {
        "Category": "\u53bb\u75f0\u85ac",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a1\u65e50.06g/\u338f\u30001\u65e53\u56de\u307e\u3067",
        "Name": "\u30e0\u30b3\u30bd\u30eb\u30d0\u30f3DS1.5%",
        "Taste": "\u30e8\u30fc\u30b0\u30eb\u30c8"
    },
    {
        "Category": "\u6297\u751f\u5264",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a1\u65e59~18\u338e/\u338f\u30001\u65e53\u56de\u307e\u3067",
        "Name": "\u30bb\u30d5\u30be\u30f3\u7d30\u7c92\u5c0f\u5150\u752810%",
        "Taste": "\u30b9\u30c8\u30ed\u30d9\u30ea\u30fc"
    },
    {
        "Category": "\u6297\u751f\u5264",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a1\u65e53\u338e/\u338f\u30001\u65e53\u56de\u307e\u3067",
        "Name": "\u30e1\u30a4\u30a2\u30af\u30c8MS\u5c0f\u5150\u7528\u7d30\u7c9210%",
        "Taste": "\u30e8\u30fc\u30b0\u30eb\u30c8"
    },
    {
        "Category": "\u93ae\u54b3\u85ac",
        "Dose": "\u5e74\u9f62\u306b\u3088\u308a8~14\u6b731\u65e59~16ml\u30013\u304b\u6708~7\u6b731\u65e53~8ml\u30001\u65e53~4\u56de\u307e\u3067",
        "Name": "\u30e1\u30b8\u30b3\u30f3\u914d\u5408\u30b7\u30ed\u30c3\u30d7",
        "Taste": "\u30c1\u30a7\u30ea\u30fc"
    },
    {
        "Category": "\u93ae\u54b3\u85ac",
        "Dose": "\u5e74\u9f62\u306b\u3088\u308a1\u6b73\u672a\u6e805~20\u338e\u30011\u6b73\u4ee5\u4e0a3\u6b73\u672a\u6e8010~25\u338e\u30013\u6b73\u4ee5\u4e0a6\u6b73\u672a\u6e8015~40\u338e\u30001\u65e53\u56de\u307e\u3067",
        "Name": "\u30a2\u30b9\u30d9\u30ea\u30f3\u656310%",
        "Taste": "\u7518\u3044"
    },
    {
        "Category": "\u6297\u30a2\u30ec\u30eb\u30ae\u30fc\u85ac",
        "Dose": "\u5e74\u9f62\u306b\u3088\u308a1\u6b73\u4ee5\u4e0a6\u6b73\u672a\u6e804\u338e\u30001\u65e51\u56de\u307e\u3067",
        "Name": "\u30b7\u30f3\u30b0\u30ec\u30a2\u7d30\u7c924\u338e",
        "Taste": "\u306a\u3057"
    },
    {
        "Category": "\u6297\u30a2\u30ec\u30eb\u30ae\u30fc\u85ac",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a7\u338e/\u338f\u30001\u65e52\u56de\u307e\u3067",
        "Name": "\u30aa\u30ce\u30f3\u30c9\u30e9\u30a4\u30b7\u30ed\u30c3\u30d710%",
        "Taste": "\u30e8\u30fc\u30b0\u30eb\u30c8"
    },
    {
        "Category": "\u93ae\u75db\u85ac",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a10~15\u338e/\u338f\u30001\u65e560\u338e/\u338f\u307e\u3067",
        "Name": "\u30ab\u30ed\u30ca\u30fc\u30eb\u7d30\u7c9220%",
        "Taste": "\u30aa\u30ec\u30f3\u30b8"
    },
    {
        "Category": "\u93ae\u75db\u85ac",
        "Dose": "\u4f53\u91cd\u3042\u305f\u308a6.5\u338e/\u338f\u30001\u65e52\u56de\u307e\u3067",
        "Name": "\u30dd\u30f3\u30bf\u30fc\u30eb\u656350%",
        "Taste": "\u306a\u3057"
    }
]

formatted_data = []

for item in data:
    formatted_item = {
        "Category": item["Category"],
        "Name": item["Name"],
        "Dose": item["Dose"],
        "Taste": item["Taste"]
    }
    formatted_data.append(formatted_item)

print(formatted_data)
