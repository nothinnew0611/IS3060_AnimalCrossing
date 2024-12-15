import streamlit as st


print("page reloaded")
st.set_page_config(
    page_title="Animal Crossing: New Horizons",
    page_icon="./images/Animal.png"
)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/O4rHCgM.png");
             background-attachment: fixed;
             background-size: cover
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title("Animal Crossing Villagers")
st.header("Let’s build your Animal Crossing village by adding new villagers!")
st.subheader("Your dream getaway begins now.", divider='rainbow')
st.write("Do you have a favorite Animal Crossing villager? 🐾  Here, you can create your very own personalized villager encyclopedia! Add the villagers you adore, explore their personalities, and build the perfect collection to showcase your dream village. 🌳✨ Start your journey now and fill your Villager Dex with all your favorites!")

personality_emoji_dict = {
    "normal": "😊",
    "lazy": "😴",
    "peppy": "🌟",
    "cranky": "😠",
    "smug": "😎",
    "snooty": "💅",
    "jock": "🏋️",
    "sisterly": "🌸",
    "cheerful": "😁",  
    "shy": "🙈",       
    "kind": "🤗",      
    "energetic": "⚡", 
    "adventurous": "🌍", 
}

initial_villagers = [
    {
        "name": "Eunwoo",
        "personality": ["energetic", "cheerful"],
        "image_url": "https://i.namu.wiki/i/EskIc0ZHQJzsSWl7yoQo3_9ZJcBQw8d311bTa3eitwiX56ja3GQv2G0-u6_u87z6lEJJT8MlRLiq4afhtrlf31l7muH6DOUAyg2aCnegjuSK2bC3LBTEjR4LbxROcRMtze3Bv7-IfkxfMx7aw_CVcw.webp",
    },
    {
        "name": "Youjeong",
        "personality": ["sisterly", "kind"],
        "image_url": "https://i.namu.wiki/i/bneIdmhltycIJl7b93RqW7pqhWM-hG8GWVBudthrSmZp4dXxot_4CJsfpC4S22IEbTwEHnoaIK_5u8xwA39PfNyFoAVQ7jMmEOB312yiPTUf3YRwneBfqpDcLtTfUZXnIGV32seCp1EOaljUJ6cGAQ.webp",
    },
    {
        "name": "Tommy",
        "personality": ["lazy", "shy"],
        "image_url": "https://i.namu.wiki/i/8P7n_vYHSPnUaJOJSiw1nzmhO4EXbEmuzoO4U2VWO8DtrEotKKEQyQgwu322lLoK-9xwY2ilmtpkJDefMvenin-38lH6Ljni6muyPhzv2XgVwCiY_1x2ldqn9sC2xSmSVH4iIL_99k43sVSyiI66aA.webp"
    },
    {
        "name": "Marshal",
        "personality": ["smug", "cranky"],
        "image_url": "https://i.namu.wiki/i/CWOZmp0dUpaa6AUeM1gxJRFifejuwxy89rHAmHpFvyVRRpcardyx_bs0JhkHmT4uVGexbczehaceRU-gYVhtttN4dQeC4TWmq0vrEisoe6ZGZxdNkuRx6paUueKJGngxFJLBps1lWMVno4s6ed57X3QLh_vBwaUW8my8jOnoJek.webp"
    },
    {
        "name": "John",
        "personality": ["normal", "jock"],
        "image_url": "https://i.namu.wiki/i/hbqICzdVfK0_ezxiv1qzpxv2h8ZHxnXDfivoFb5hZSY7jH7d4EY2fT8mHCrNbuyOlpmxIuRPqH33UXGCRVGIgLBzj7oiiJLaTJdrGn29sNiNKRzZnfRnA0qlmdmUNR-NzU7nLgH6dWT_iB5CoV2iLA.webp",
    },
    {
        "name": "Vanilla",
        "personality": ["sisterly", "peppy"],
        "image_url": "https://i.namu.wiki/i/3Ka4ju_-z2gUlrs-LQGr9NJ-Bn8SAHnuV-3uiGRWyGRLz9FuCD7JVzZZGIlHnq-tU7RPaS0xAyIR5zCfRxqANOeb0x3XxUq_V9k9PSf7ukeSv4Vzj4OoVEN1qjt1TfsfmX5foP3_d9QkSB25gd1bVw.webp",
    },
    {
        "name": "Caramel",
        "personality": ["cheerful", "energetic"],
        "image_url": "https://i.namu.wiki/i/DjjczQEPlzvJEv9rVz1zmvK6_XCD_Rv8w3wibMRYNs7w8eYR3Eweh17UXJJ6X1cIyfVsdBa2hm_WBJW0POmcJzinYs0zhs7erOWWT2QAVRhyYLoOjtGxR-sw79w6u3R4A895iW_rSAwfjNuqubf1OA.webp"
    },
    {
        "name": "Bagel",
        "personality": ["cranky", "smug"],
        "image_url": "https://i.namu.wiki/i/LHRCW32Vk04MwwomYfn14ypVW7HGjv0Ra00OHhCaiyHy-GeLYCWGYpaoWZFvKUTOoQ0n1mitqjKyWE-RtCjOqIY0HgvDajCTpqiA93oZY11rh4V7ujXfcm5Q30tcym1iTxqaCbCEel-Z6wEukWPjog.webp"
    },
    {
        "name": "Edward",
        "personality": ["snooty", "kind"],
        "image_url": "https://i.namu.wiki/i/bmxNEi9IfXFd6s7bMyymt-Sqf_9rCrtO5pXen4jQI5EYlJB3ljI2UHIXHvCCG40mH63YzVS-BYTMmmZ_rYyK-Kj5f7oZzhC-0wKONc9JVNre5nyAasXJWuYg8om6zLYabXaeLVpUZuZR98eIsV6VKA.webp"
    },
    {
        "name": "Hannah",
        "personality": ["sisterly", "smug"],
        "image_url": "https://i.namu.wiki/i/WK5zIfEZ54NAMSsvf8U7kImpkN3_d2lyAlA7Wj6__TsHDNn5bwjnDwoer82xlmx3I75_Z1ze0UWZnsFtGm7fLesnzrlDIa1FSSAaF191L4hDdicKbBisZGkKamWwkPxuieZHg01ktUv8JItLKHQD5w.webp"
    },
    {
        "name": "Champ",
        "personality": ["energetic", "adventurous"],
        "image_url": "https://i.namu.wiki/i/3GrmY-k890nOdsfJBVGodZCPGuqSSbSlQiOBcQHJcAC2WvcvA5Sx5yyHarwCkHiDJFf0cgWENVPpme1OJgwYRVBS7LeEswBhGx02QzVTFcRK7BXIvIClHFxvqLZW5whL5dJ9GZqqaUhhjbVSZQu2pQ.webp"
    },
    {
        "name": "Blender",
        "personality": ["cheerful", "peppy"],
        "image_url": "https://i.namu.wiki/i/VrPhCzb4VspNHUYtyQFr9XY9CPMIYKOwOFMqJZ0MvW8IgPyZLBN-CNClQYO02cMYJIWNEs57syL_qDL0So-G0ZQHFQe1fWbdsOh4d19GvsF9Ih1CAQJA_tY-Jx-UOUQDN87eIxmTEAcwWkZt7e9yuA.webp"
    },
]

example_villager = {
    "name": "Berry",
    "personality": ["adventurous", "sisterly"],
    "image_url": "https://i.namu.wiki/i/91YMX-8cpFQWX407qzmWfREkaQ4L5_OmXwFRiB5-7loPK02EoGUMPleXLjrHWnfHOHKh110wsUI4pt7R0S7jLLTjy6gUdJCidvhZ1fqbIs16ypDCFr9aiMy_a7t_DYfzWq2o_sbf-LnkaqzEmW4U4g.webp"
}



if "villagers" not in st.session_state:
    st.session_state.villagers = initial_villagers



auto_complete = st.toggle("Fill with example data")
print("page_reload, auto_complet", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
                label="Villager Name",
                value=example_villager["name"] if auto_complete else ""
            )
    with col2:
        personality = st.multiselect(
            label="Villagers' Personality", 
            options=list(personality_emoji_dict.keys()),
            max_selections=2,
            default=example_villager["personality"] if auto_complete else []
        )
    image_url = st.text_input(
        label="Villager Image URL",
        value=example_villager["image_url"] if auto_complete else ""
    )    
    submit = st.form_submit_button(label="submit")
    if submit:
        if not name:
            st.error("Please enter the name of the Villager.")
        elif len(personality) == 0:
            st.error("Please select at least one Villager's personality.")
        else:
            st.success("The villager has been successfully added to your collection!")
            st.session_state.villagers.append({
                "name": name,
                "personality": personality,
                "image_url": image_url if image_url else "./images/crossing.png"
            })




for i in range(0, len(st.session_state.villagers), 3):
    row_villagers = st.session_state.villagers[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_villagers)):
        with cols[j]:
            villager = row_villagers[j]
            with st.expander(label=f"**{i+j+1}. {villager["name"]}**", expanded=True):
                st.image(villager["image_url"])
                emoji_personality = [f"{personality_emoji_dict[x]} {x}" for x in villager["personality"]]
                st.subheader(" / ".join(emoji_personality))
                delete_button = st.button(label="delete", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.villagers[i+j]
                    st.rerun()

st.slider("How many villagers would you like to collect for your village?",min_value=1, max_value=100)