from deep_translator import GoogleTranslator

def main():
    print("영어 → 한국어 번역 프로그램")    
    
    english_text = '''
With fighter jets, a red carpet and a hopeful slogan — “Pursuing Peace” — plastered on the wall, President Donald Trump welcomed his Russian counterpart Vladimir Putin for a summit in Alaska on Friday whose results remained entirely unclear once it abruptly ended.
After meeting for nearly three hours, the two men emerged to proclaim progress. But they exited their scheduled news conference without explaining what, exactly, they have achieved.
One thing that was evident: There was no deal made. And the ceasefire Trump said he wanted in place when the summit ended was far from becoming a reality as he increasingly put the onus on Ukrainian President Volodymyr Zelensky to “make a deal.”
'''
    try:
        korean_text = GoogleTranslator(source='en', target='ja').translate(english_text)
        print("원문 영어: ", english_text)
        print("자연스러운 한국어 번역: ", korean_text)
        print("-" * 50)
    except Exception as e:
        print("번역 중 오류가 발생했습니다:", e)
        print("-" * 50)

if __name__ == "__main__":
    main()
