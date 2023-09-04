# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:25:28 2023

@author: swann
"""

import dotenv
import os
import openai

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

openai.api_key = os.getenv("OPENAI_API_KEY")


#def run_gpt(data):
def run_gpt():
    
    
    #condition = data['condition']
    #context = data['context']
    
    condition = '치킨 알레르기, 고혈압'
    context = '탕수육 만드는법/이연복 탕수육 레시피 : : 집에서도 바삭하고 맛있는 탕수육만들기 :)주말에 백종원 만능춘장으로 해물짜장하고 탕수육도 해먹었어요 ^^달달하고 상큼하고 바삭한 탕수육은 정말 남녀노소~저도 어릴때도 완전 좋아했지만 다큰 지금도 가끔 먹으면 넘 맛나죠~~여러 레시피로 해보고 최선이었던 레시피로 올려봐요바삭하고 소스도 맛있는 탕수육 레시피!★ \xa0<탕수육(3-4인)>돼지고기 등심이나 안심 한근, 파프리카 노랑빨강 1/4개씩, 오이 1/4개, 양파 1/4개(채소는 냉장고 사정에 맞게~)고기밑간 : 소금 후추 솔솔솔(굳이 따지면 소금 2작은술, 후추 1/2작은술 정도)튀김옷 : 녹말가루(감자,고구마,옥수수 전분중 아무거나) 600ml, 물 300ml(녹말 : 물을 2:1로 준비하시면 돼요~) + 달걀흰자 1개탕수육 소스 : 물 300ml, 간장 3큰술, 식초 3큰술, 설탕 6큰술, 굴소스 1/3큰술, 생강즙 1큰술(생강가루로 대체하거나 없으면 생략ok)(간장식초설탕 1:1:2 비율)1. 먼저 정육점가셔서 안심이나 등심으로 탕슉 하신다고 잘라달라고 하시면 요로케 주세요,소금 후추 솔솔 뿌려서 뒤적뒤적 밑간하고..\xa02. 채소는 냉장고 상황따라 준비하세요~저는 당근이랑 목이버섯도 넣었어요 :)파프리카 노랑빨강 1/4개씩, 오이 1/4개, 양파 1/4개(채소는 냉장고 사정에 맞게~)\xa0이제부터 제일 중요한거탕슉은 뭐다?빠삭함 + 소스 이 두가지가 핵오브더핵이죠..제가 올린 레시피는 제가 즐겨보는 요리블로거 다소마미님 레시피구요,직접해보니 바삭하고 맛있었어요.근데 저는 사실 중식집처럼 완전 딱!딱!할정도의 바삭함을 만들어 보고파서..일요일에는 이연복쉐프님 레시피로 해봤거든요그거는.. 아예 녹말가루랑 물을 녹말가루 잠길정도로 부어주고 2-3시간 기다리면아래쪽에 녹말, 위에는 물 이렇게 완전히 분리가돼요.그럼 위에 물은 다 따라버리고 밑에 남은 딱딱한 녹말가루에 식용유 4큰술과 계란 흰자 하나를 넣고열심히 손으로 주물럭 주물럭 잘 섞어서 반죽하는건데..그렇게 했는데 반죽이 너무 딱딱해서 고기에 잘 안달라붙어서 너무 튀김옷 없는 소고기튀김처럼 되버리더라구요 ㅠㅠ제가 뭔가 잘못한거 같은데 알수없고.. ㅋㅋㅋ또 이 레시피는 녹말가루가 완전히 물이랑 분리되게 2시간은 둬야해서 시간도 걸리구요..고구마전분 옥수수전분을 7:3비율로 섞으라고돼있어서 전분도 여러가지 사와야해..그래도 정말 중식집의 빠삭함이 나왔다면 그걸 올렸을텐데 저는 실패하여..구구절절 스토리가 긴데 하여간 지금 올리는 이 레시피로도 충분히 바삭하고 맛있어서 요고 올려요 ^^3. 녹말가루(감자,고구마,옥수수 전분중 아무거나) 600ml, 물 300ml(녹말 : 물을 2:1로 준비하시면 돼요~) + 달걀흰자 1개\xa0위 분량대로 넣고 잘 섞어주세요~약간 또르르 떨어지는 살짝 진득한 정도 농도 나와요 ㅎㅎ\xa04. 이제 튀김냄비에 기름을 넉넉히 붓고..반죽 살짝 떨어트려서 2-3초 정도 후에 반죽이끓어오르는 온도 되면 고기 넣고 열심히 튀기기 ^^* 튀김은 자고로 요로케 너무 넓지 않고 폭은 깊은 뚝배기같은 그릇에 튀기는게 좋아요.어차피 기름에 퐁당 담가야 하기때문에 후라이팬같이 넓은데 하면 기름만 엄청 많이 드니까 ㅎㅎ그래서 저는 튀김전용 뚝배기를 하나 두고 여기엔 튀김만 해요 ㅋㅋㅋ버릴땐 절대 그냥 버리면 안되구 우유팩에 신문 뭉치고, 폐기름 붓고, 또 신문 뭉치고, 폐기름 붓고 해서분리수거 종이쪽에다 버리기~ *\xa0모든튀김은 그리고 2번 튀겨야 바삭하고 맛나요 꼭 두번튀겨주세요~~손님 오실땐 미리 튀겨두고 오시면 다시 튀겨서 내면 딱!1차 초벌튀김한 모습이에요 ㅎㅎ2번튀기니 조금더 베이지색이 됐는데 그 사진은 없음 급히 상에 올리느라 ^^;\xa0자 이제 탕슉의 또 하나의 최중요한 덕목 ㅋㅋㅋ소오스~소스는 연복 쉐프님 레시피 고대로 했더니 딱 맛있더라구요 ^^사과식초만 넣었는데도 과일넣은거같이 상큼하고..딱 조은 짭짤 달큰 상큼한 바로 그 소오스~~♥5.  물 300ml, 간장 3큰술, 식초 3큰술, 설탕 6큰술, 굴소스 1/3큰술, 생강즙 1큰술(생강가루로 대체하거나 없으면 생략ok)(간장식초설탕 1:1:2 비율)=> 위 분량대로 먼저 소스만 넣고 끓이다가 끓어오르면! 채소들 넣고 살짝 끓이고,불을 끈뒤! 녹말가루랑 물을 1:1 비율로 섞어서 (한 5수저 정도씩 넣고 섞으면 되실거에요),조금씩 넣고 저어주고 넣고 저어주면서 농도 걸쭉해지면 마무리!\xa0\xa0탕슉은 역시 찍먹이니라..부먹도 조아하지만 손님들 취향 모를땐 찍먹으로 내는게 딱이지여 ㅋㅋ주말에 이틀연속 탕수육을 하느라여러 버전 반죽해보고 직접 해보고 먹어보고 쓰는 최종 탕슉 레시피..ㅋㅋ일욜에는 사실 연복쉐프님거 반죽으로 잘 안돼서걍 손대중으로 반죽했더니 토욜보다 또 더 잘됐거든요..녹말가루를 한\xa03 : 물 1로 더 뻑뻑하게 했던거 같은데 정확히 계량을 안해서 못올리겠다탕수육 또 해보고 더 완벽한 레시피가 생기면 수정해볼게요ㅋㅋㅋㅋㅋㅋㅋ위 레시피로도 충분히 바삭하고 맛나니엊그제 올린 만능춘장으로 짜장면이랑 콤보로 해서 드셔보세요.날씨도 시원해져서 튀김도 할만하자네~둘다 너무너무 맛나요~손님초대용으로도 강추!!\xa0\xa0\xa0'
    
    prompt = f"""
First of all, correct the words in context if the spell is incorrect. For example, there isn't '모기버섯', '목이버섯' is correct.
If the recipe is suitable for {condition} in its current state, let it be and say "그대로 사용하셔도 좋은 레시피네요! 영상에서 레시피를 추출해드릴게요" and just extract and arrange the recipe accordingly in the response.
And arrange the list of recipe from following {context}, replace the ingredients and revise the recipe with good taste according to my condition: {condition}.
In addition, I'd like that the food made by revised recipe tastes good.
Answer in Korean. Please give bad and new ingredients separately for me in some health condition in the form of lists.
If the spelling is incorrect in Korean, revise them to correct words. For example, '모기버섯' to '목이버섯'.
And do not say the word '대체' or '대체재,' just give me detailed and revised ingredients I can search with the ingredient's name. For example, '설탕 대체재' to '스테비아'.
Give me the recipe with the weight of the ingredients to weigh easily for home cook.
The replaced ingredients should be the thing we can get easily at home.
context: {context}
Give me output which is as following format with JSON and not with any descriptions.
And finish the recipe with a word of advice.
Example Answer for diabetes:
{{
  "recipe_name": "당뇨 환자를 위한 요리법"
  "bad": ["설탕", "등심", "전분", "달걀 흰자", "간장"],
  "good": ["스테비아", "닭 가슴살", "콩가루", "달걀 흰자 대체재(아쿠아파바)", "간장 대체재(코코아미노)"],
  "ingredients": [
    {{"name": "닭 가슴살", "amount": "150g"}},
    {{"name": "당근", "amount": "1/2개"}},
    {{"name": "오이", "amount": "1/2개"}},
    {{"name": "목이버섯", "amount": "50g"}},
    {{"name": "파인애플", "amount": "1/4개"}},
    {{"name": "스테비아", "amount": "5큰술"}},
    {{"name": "식초", "amount": "4큰술"}},
    {{"name": "코코아미노", "amount": "2큰술"}},
    {{"name": "콩가루", "amount": "1/2컵"}},
    {{"name": "아쿠아파바", "amount": "1개"}},
    {{"name": "물", "amount": "1컵 + 3분의 1컵"}}
  ],
  "recipe": [
    "1. 닭 가슴살을 편으로 썰어줍니다.",
    "2. 당근, 오이, 목이버섯, 파인애플을 적당한 크기로 썰어줍니다.",
    "3. 콩가루와 아쿠아파바를 섞어 튀김옷을 만듭니다.",
    "4. 닭 가슴살을 튀김옷에 묻혀 170-180도의 기름에서 5-6분 동안 튀깁니다.",
    "5. 물 1컵에 스테비아, 식초, 코코아미노를 넣고 섞어 소스를 만듭니다.",
    "6. 소스가 끓기 시작하면 콩가루와 물을 섞어 물전분을 만들고 소스에 부어줍니다.",
    "7. 튀긴 닭 가슴살을 소스에 묻히고 잘 섞어줍니다.",
    "8. 접시에 담아 완성합니다."
  ],
  "advice":"이 레시피는 건강을 위해 보조적으로 활용될 뿐이며, 특정 질환의 치료를 위해서는 가까운 병원을 찾아주시기 바랍니다."
}}
"""

    
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a cooking expert bot who can revise recipes according to individual health status.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    res = completion.choices[0].message["content"]
    print(res)
    return res

