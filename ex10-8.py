import json

member={"id":"swhong",
        "name":"홍성우",
        "age":23,
        "history":[{"date":"2025-08-12", "route":"mobile"},
                   {"date":"2025-07-12", "route":"pc"}]
                   }

with open("member.json", "w", encoding="utf-8") as f:
    
# json_string = json.dumps(member, ensure_ascii=False, indent=4)
        # dump() : 딕셔너리를 json 파일로 생성
        json.dump(member, f, ensure_ascii=False, indent=4)        