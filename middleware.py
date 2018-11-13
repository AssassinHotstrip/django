# 定义中间件函数

def my_middleware(get_response):
    print("init middleware")

    def middleware(request, *args, **kwargs):

        print("before request 被调用")

        response = get_response(request, *args, **kwargs)

        print("after request 被调用")
        return response

    return middleware


def my_middleware2(get_response):
    print("init middleware2")

    def middleware(request, *args, **kwargs):

        print("before request2 被调用")

        response = get_response(request, *args, **kwargs)

        print("after request2 被调用")
        return response

    return middleware
