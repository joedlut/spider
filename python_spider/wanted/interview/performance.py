import logging
from . import dingtalk
import time
import traceback
from sentry_sdk import capture_exception
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# 参数固定写 get_response
def performance_logger_middleware(get_response):
    def middle(request):
        start_time = time.time()

        # 处理完请求
        response = get_response(request)
        duration = time.time() - start_time
        response["X-Page-Duration-ms"] = int(duration * 1000)
        logging.info("%s %s %s",duration*1000,request.path,request.GET.dict())
        return response
    # 返回的是中间件函数名
    return middle

# 使用中间件类替换上面的方法 记录时耗，处理异常
class PerformanceAndExceptionLoggerMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response["X-Page-Duration-ms"] = int(duration * 1000)
        logger.info("duration:%s url:%s parameters new interface :%s", duration, request.path, request.GET.dict())
        return response

    def process_exception(self, request, exception):
        if exception:
            message = "url:{url} ** msg:{error} ````{tb}````".format(
                url=request.build_absolute_uri(),
                error=repr(exception),
                tb=traceback.format_exc()
            )

            logger.warning(message)

            # send dingtalk message
            dingtalk.send(message)

            # capture exception to sentry:
            capture_exception(exception)

        return HttpResponse("Error processing the request, please contact the system administrator.", status=500)



