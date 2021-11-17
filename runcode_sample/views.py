import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from runcode import Runner


def run_code(request):
    # runner = Runner(
    #     api_key="KMXQosOYD1Bmrg1OJg4PzaQyprVVXaYkCsv3HgTh",
    #     callback_url="http://7a91-2405-201-c00a-e012-4abc-50aa-3eb3-71d5.ngrok.io",
    # )
    runner = Runner()
    runner.execute(
        code="""
print("Hello world")
start = input()
end = input()
for i in range(int(start), int(end)):
    print(i)
""",
        input="1\n10",
        compiler=Runner.python39,
        extra_params={"ukey": "16"},
    )

    return HttpResponse("hi")


@csrf_exempt
def test_index(request):
    received_json_data = json.loads(request.body)
    print(received_json_data)
    return HttpResponse("ok")
