

preferred_items = {}
store = {"EAppliances": ["Pan", "Kettle"],
         "Clothes": ["Shorts", "Dresses"]}
def add_user(user_id, category):
    preferred_items[user_id] = category
def recommendation(user_id):
    recommended_items = []
    for category in user_category:
        if category in store:
            recommended_items.extend(store[category])
    return recommended_items
add_user(1, ["Electronics", "Groceries"])
print(recommendation(1))








