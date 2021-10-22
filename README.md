# RunCode Python API

This API is as simaple as send your code and getting execution result. 

Install 

```
pip install runcode
```



## Python Example
```
from runcode import Runner

runner = Runner(
    api_key="",
    callback_url="",
)

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
    )
    
```
You need to provide two parameters here.  
api_key - you will get it from runcode.io dashboard after loging.  
callback_url - Your application URL to process execution result.  
compiler - You can choose any of the available compilers from RunCode docs.
## Django Example
```
from runcode import Runner

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
    )
```
You need to specify compiler here.
compiler - You can choose any of the available compilers from RunCode docs.

You need to add two parameters to settings.py file.

RUNCODE_API_KEY - you will get it from runcode.io dashboard after loging.  
RUNCODE_CALLBACK_URL - Your application URL to process execution result. 

### Available compilers
```
python39 = "python-3.9.7"
gcc49 = "gcc-4.9"
cpp49 = "g++-4.9"
openjdk11 = "openjdk-11"
dotnet5 = "dotnet-5"
python27 = "python-2.7.18"
php81 = "php-8.1"
fsharp5 = "fsharp-5"
ruby30 = "ruby-3.0.2"
```


For further support, contact hello@runcode.io 
