import requests


class Runner:

    python39 = "python-3.9.7"
    gcc49 = "gcc-4.9"
    cpp49 = "g++-4.9"
    openjdk11 = "openjdk-11"
    dotnet5 = "dotnet-5"
    python27 = "python-2.7.18"
    php81 = "php-8.1"
    fsharp5 = "fsharp-5"
    ruby30 = "ruby-3.0.2"

    def __init__(self, api_key="", callback_url=""):
        """
        Constructs and sends a :class:`Runner <Runner>`.
        :param api_key: API Key to autheticate and process your request. You can get it in runcode.io dashboard.
        :param callback_url: URL to receive executon results.
        :return: :class:`Runner <Runner>` object
        :rtype: runcode.Runner
        Usage::
        >>> from runcode import Runner
        >>> runner = Runner(
                api_key="{API_KEY}",
                callback_url="{URL_TO_PROCESS_RESULT}",
            )
        """

        if api_key == "":
            try:
                from django.conf import settings

                self.api_key = settings.RUNCODE_API_KEY
                self.callback_url = settings.RUNCODE_CALLBACK_URL
            except:
                pass
        else:
            self.api_key = api_key
            self.callback_url = callback_url

    def execute(self, code, input, compiler, extra_params={}):
        """
        Sends code and input to be executed by runcode platform.
        :param code: Code to get executed.
        :param input: input values for the code.
        :compiler: Compiler to use to execute the code.
        :extra_params: json dict to post extra parameters to identify the response or any other purpose
        Usage::
        >>> runner.execute(
                code='''
                print("Hello world")
                start = input()
                end = input()
                for i in range(int(start), int(end)):
                    print(i)
                ''',
                        input="1\n10",
                        compiler=Runner.python39,
            )
        """

        out = {
            "api_key": self.api_key,
            "code": code,
            "input": input,
            "compiler": compiler,
            "callback_url": self.callback_url,
            "extra_params": extra_params,
        }

        r = requests.post("https://app.runcode.io/api/run-code/", json=out)
        # r = requests.post("http://localhost:8000/api/run-code/", json=out)
