from tools.tavily_search import TavilySearcher

from dotenv import load_dotenv
load_dotenv()

class TestTavilySearcher:
    searcher = TavilySearcher(max_results=3).get_tavily_searcher()

    def test_search(self):
        reply = self.searcher.invoke("Federated learning")

        assert type(reply) is dict
        assert type(reply['results']) is list

        for r in reply['results']:
            print(r['content'])
            print(f"Source: {r['url']}")
            print('~'*80)

if __name__=='__main__':
    tester = TestTavilySearcher()
    tester.test_search()
