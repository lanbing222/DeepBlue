'''
Created on 2018/7/8

@author: Administrator
'''
from django.http import HttpResponse
def helloworld(request):
    return HttpResponse('helloworld')

if __name__ == '__main__':
    pass