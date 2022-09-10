import re
import traceback
import typing as ty

import pytube
from backend.apps.ai.hanspell import spell_checker
from krwordrank.word import summarize_with_keywords
from youtube_transcript_api import YouTubeTranscriptApi

# from hanspell import spell_checker

sample_url = "https://www.youtube.com/watch?v=mc02IZhouEg"
sample_url2 = "https://youtu.be/mc02IZhouEg"
sample_slug = "mc02IZhouEg"


class YoutubeInference:
    youtube_id_compiler = re.compile("(v=)([a-zA-Z0-9-_]{11})")
    stop_words_path = "backend/apps/ai/stopwords.txt"
    # stop_words_path = "stopwords.txt"

    youtube_url_prefix = "https://www.youtube.com/watch?v="

    with open(stop_words_path, "r", encoding="utf-8") as fp:
        stop_words = fp.readline().strip().split()

    # hyper parmas
    beta = 0.85  # PageRank의 decaying factor beta
    max_iter = 10
    min_count = 2  # 단어의 최소 출현 빈도수 (그래프 생성 시)
    max_length = 10  # 단어의 최대 길이
    verbose = True

    def __init__(self, slug: str = sample_slug):
        self._url = self.youtube_url_prefix + slug
        try:
            yt = pytube.YouTube(self._url)
        except Exception:
            traceback.print_exc()
            return Exception
        self._title = yt.title
        self._thumbnail = yt.thumbnail_url
        self._author = yt.author

    @property
    def url(self) -> str:
        return self._url

    @property
    def thumbnail_url(self) -> str:
        return self._thumbnail

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    def inference(self) -> ty.List[dict]:
        try:
            (
                scripts_info,
                scripts,
            ) = self.get_transcript()  # {00:01: {"script":"가나다라마바사"}} 형식

            word_importance = self.get_script_keywords(scripts)  # 무슨 단어가 몇 점인지

            scripts_info, keywords_info, words_freq = self.get_script_importance(
                scripts_info, word_importance
            )
            return scripts_info, keywords_info, words_freq
        except Exception:
            traceback.print_exc()
            return None

    def get_transcript(self, lang: str = "ko") -> ty.Dict[str, dict]:
        youtube_id: str = self.gen_youtube_id(self.url)
        scripts: dict = YouTubeTranscriptApi.get_transcript(
            youtube_id, languages={lang}
        )

        res = []
        s = []
        for script in scripts:
            time_str = self.time_int_to_str(script["start"])
            processed_script = self.preprocessing(script["text"])
            s.append(processed_script)
            rets = {}
            rets[time_str] = {
                "script": processed_script,
                "importance": 0,
            }
            res.append(rets)

        return res, s

    def get_script_keywords(self, scripts):
        keywords = summarize_with_keywords(
            texts=scripts,
            min_count=self.min_count,
            max_length=self.max_length,
            beta=self.beta,
            max_iter=self.max_iter,
            stopwords=self.stop_words,
            verbose=self.verbose,
        )

        word_importance = {}

        for word, importance in sorted(
            keywords.items(), key=lambda x: x[1], reverse=True
        )[:20]:
            word_importance[word] = importance
        return word_importance

    def get_script_importance(self, scripts_info, word_importance):
        keywords_info = []
        words_freq = {}

        for i in range(len(scripts_info)):
            info = scripts_info[i]

            timestamp = list(info.keys())[0]
            text = info[timestamp]["script"].split()
            intersection = set(word_importance.keys()).intersection(set(text))
            word_count = len(intersection)
            for word in intersection:
                if words_freq.get(word) is None:
                    words_freq[word] = 1
                else:
                    words_freq[word] += 1

                keywords_info.append(
                    {
                        "keyword": word,
                        "timestamp": timestamp,
                        "score": word_importance[word],
                    }
                )

            scripts_info[i][timestamp]["importance"] += word_count

        return scripts_info, keywords_info, words_freq

    def gen_youtube_id(self, url):
        return self.youtube_id_compiler.search(url).group(2)

    def time_int_to_str(self, start_time):
        minute = str(int(start_time) // 60)
        second = str(int(start_time) - int(minute) * 60)
        if len(minute) == 1 and len(second) == 1:
            # 초와 분 둘 다 한자리 숫자이면
            ret = "0" + minute + ":0" + second
        elif len(minute) == 1:
            # 분이 한자리 숫자이면
            ret = "0" + minute + ":" + second
        elif len(second) == 1:
            # 초가 한자리 숫자이면
            ret = minute + ":0" + second
        else:
            ret = minute + ":" + second
        return "00:" + ret

    def preprocessing(self, script):
        new_script = re.sub("\n", "", script)
        new_script = re.sub("[a-zA-Z]", "", new_script)
        new_script = re.sub("\d+", "", new_script)
        new_script = re.sub("[ㄱ-ㅎㅏ-ㅣ]+", "", new_script)
        new_script = re.sub(
            "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", new_script
        )
        new_script = spell_checker.check(new_script).checked

        return new_script


yi = YoutubeInference("O4xuYk20J40")
scripts_info, keywords_info, words_freq = yi.inference()
# import pprint

# pprint.pprint(scripts_info)
# pprint.pprint(keywords_info)
# pprint.pprint(words_freq)
