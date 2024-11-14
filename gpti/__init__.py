import requests
import json
from .util import api, nexra, apistrm

class gpt:
    class v1:
        def __init__(self, messages=[], prompt="", model="", markdown=False):
            try:
                data_ = {
                    "messages": [],
                    "prompt": "",
                    "model": "GPT-4",
                    "markdown": False
                }

                try:
                    mess = []
                    pro = ""
                    mod = "GPT-4"
                    mark = False

                    if messages is not None:
                        mess = messages
                    if prompt is not None:
                        pro = prompt
                    if model is not None:
                        mod = model
                    if markdown is not None and markdown == True:
                        mark = True
                    
                    data_ = {
                        "messages": mess,
                        "prompt": pro,
                        "model": mod,
                        "markdown": mark
                    }
                except Exception as e:
                    data_ = {
                        "messages": [],
                        "prompt": "",
                        "model": "GPT-4",
                        "markdown": False
                    }
                
                try:
                    res_ = api(data=data_, api="https://nexra.aryahcr.cc/api/chat/gpt", image=False)
                    self.__error = res_.error()
                    self.__result = res_.result()
                except Exception as e:
                    self.__error = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    self.__result = None
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
            pass
        def error(self):
            return self.__error
        def result(self):
            return self.__result
    class v2:
        def __init__(self, messages=[], stream=False, markdown=False) -> None:
            try:
                data = {
                    "messages": [],
                    "model": "chatgpt",
                    "markdown": False,
                    "stream": False
                }

                strm = False
                try:
                    if stream != None and stream == True:
                        strm = True
                    else:
                        strm = False
                except Exception as e:
                    strm = False
                
                try:
                    mess = []
                    mark = False

                    if messages is not None:
                        mess = messages
                    
                    if markdown is not None:
                        mark = markdown

                    data = {
                        "messages": mess,
                        "model": "chatgpt",
                        "markdown": mark,
                        "stream": strm
                    }
                except Exception as e:
                    data = {
                        "messages": [],
                        "model": "chatgpt",
                        "markdown": False,
                        "stream": strm
                    }

                try:
                    res_ = apistrm(data=data, api="https://nexra.aryahcr.cc/api/chat/complements", stream=strm)
                    self.__error = res_.error()
                    self.__result = res_.result()
                    self.__sttrm = res_.stream()
                except Exception as e:
                    self.__error = {
                        "code": 500,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    self.__result = None
                    self.__sttrm = None
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
                self.__sttrm = None
            pass
        def stream(self):
            if self.__sttrm != None:
                for data in self.__sttrm:
                    yield data
            else:
                yield None
        def error(self):
            return self.__error
        def result(self):
            return self.__result
    class web:
        def __init__(self, prompt="", markdown=False):
            try:
                data_ = {
                    "prompt": "",
                    "markdown": False
                }

                try:
                    pro = ""
                    mark = False

                    if prompt is not None:
                        pro = prompt
                        
                    if markdown is not None and markdown == True:
                        mark = True
                    
                    data_ = {
                        "prompt": pro,
                        "markdown": mark
                    }
                except Exception as e:
                    data_ = {
                        "prompt": "",
                        "markdown": False
                    }
                
                try:
                    res_ = api(data=data_, api="https://nexra.aryahcr.cc/api/chat/gptweb", image=False)
                    self.__error = res_.error()
                    self.__result = res_.result()
                except Exception as e:
                    self.__error = {
                        "code": 500,
                        "status": False,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    self.__result = None
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
            pass
        def error(self):
            return self.__error
        def result(self):
            return self.__result
    class v3:
        def __init__(self, messages=[], stream=False, markdown=False) -> None:
            try:
                data = {
                    "messages": [],
                    "model": "gpt-4o",
                    "markdown": False,
                    "stream": False
                }

                strm = False
                try:
                    if stream != None and stream == True:
                        strm = True
                    else:
                        strm = False
                except Exception as e:
                    strm = False
                
                try:
                    mess = []
                    mark = False

                    if messages is not None:
                        mess = messages
                    
                    if markdown is not None:
                        mark = markdown

                    data = {
                        "messages": mess,
                        "model": "gpt-4o",
                        "markdown": mark,
                        "stream": strm
                    }
                except Exception as e:
                    data = {
                        "messages": [],
                        "model": "gpt-4o",
                        "markdown": False,
                        "stream": strm
                    }

                try:
                    res_ = apistrm(data=data, api="https://nexra.aryahcr.cc/api/chat/complements", stream=strm)
                    self.__error = res_.error()
                    self.__result = res_.result()
                    self.__sttrm = res_.stream()
                except Exception as e:
                    self.__error = {
                        "code": 500,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    self.__result = None
                    self.__sttrm = None
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
                self.__sttrm = None
            pass
        def stream(self):
            if self.__sttrm != None:
                for data in self.__sttrm:
                    yield data
            else:
                yield None
        def error(self):
            return self.__error
        def result(self):
            return self.__result

class imageai:
    def __init__(self, prompt="", model="", response="url", data={}) -> None:
        try:
            data_app = {
                "prompt": "",
                "model": "",
                "data": {},
                "response": "url"
            }

            try:
                prompt_ = ""
                model_ = ""
                response_ = "url"
                data_ = {}

                if prompt is not None:
                    prompt_ = prompt
                
                if model is not None:
                    model_ = model
                
                if response is not None:
                    response_ = response
                
                if data is not None:
                    data_ = data

                data_app = {
                    "prompt": prompt_,
                    "model": model_,
                    "data": data_,
                    "response": response_
                }
            except Exception as e:
                data_app = {
                    "prompt": "",
                    "model": "",
                    "data": {},
                    "response": "url"
                }

            try:
                res_ = api(data=data_app, api="https://nexra.aryahcr.cc/api/image/complements", image=True)
                self.__error = res_.error()
                self.__result = res_.result()
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
        except Exception as e:
            self.__error = {
                "code": 500,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__result = None
        pass
    def error(self):
        return self.__error
    def result(self):
        return self.__result

class bing():
    def __init__(self, messages=[], conversation_style="", markdown=False, stream=False) -> None:
        try:
            strm = False
            data = {
                "messages": [],
                "conversation_style": "Balanced",
                "model": "Bing",
                "markdown": False,
                "stream": False
            }

            try:
                if stream != None and stream == True:
                    strm = True
                else:
                    strm = False
            except Exception as e:
                strm = False
            
            try:
                data = {
                    "messages": messages if messages is not None else [],
                    "conversation_style": conversation_style if conversation_style is not None else "Balanced",
                    "markdown": markdown if markdown is not None else False,
                    "stream": strm if strm is not None else False,
                    "model": "Bing"
                }
            except Exception as e:
                data = {
                    "messages": [],
                    "conversation_style": "Balanced",
                    "model": "Bing",
                    "markdown": False,
                    "stream": False
                }

            try:
                res_ = apistrm(data=data, api="https://nexra.aryahcr.cc/api/chat/complements", stream=strm)
                self.__error = res_.error()
                self.__result = res_.result()
                self.__sttrm = res_.stream()
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
        except Exception as e:
            self.__error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__result = None
            self.__sttrm = None
        pass
    def stream(self):
        if self.__sttrm != None:
            for data in self.__sttrm:
                yield data
        else:
            yield None
    def error(self):
        return self.__error
    def result(self):
        return self.__result

class blackbox():
    def __init__(self, messages=[], websearch=False, markdown=False, stream=False) -> None:
        try:
            strm = False
            data = {
                "messages": [],
                "websearch": False,
                "model": "blackbox",
                "markdown": False,
                "stream": False
            }

            try:
                if stream != None and stream == True:
                    strm = True
                else:
                    strm = False
            except Exception as e:
                strm = False
            
            try:
                data = {
                    "messages": messages if messages is not None else [],
                    "websearch": websearch if websearch is True else False,
                    "markdown": markdown if markdown is not None else False,
                    "stream": strm if strm is not None else False,
                    "model": "blackbox"
                }
            except Exception as e:
                data = {
                    "messages": [],
                    "websearch": False,
                    "model": "blackbox",
                    "markdown": False,
                    "stream": False
                }

            try:
                res_ = apistrm(data=data, api="https://nexra.aryahcr.cc/api/chat/complements", stream=strm)
                self.__error = res_.error()
                self.__result = res_.result()
                self.__sttrm = res_.stream()
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
                self.__sttrm = None
        except Exception as e:
            self.__error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__result = None
            self.__sttrm = None
        pass
    def stream(self):
        if self.__sttrm != None:
            for data in self.__sttrm:
                yield data
        else:
            yield None
    def error(self):
        return self.__error
    def result(self):
        return self.__result

class llama():
    def __init__(self, messages=[], markdown=False, stream=False) -> None:
        try:
            strm = False
            data = {
                "messages": [],
                "model": "llama-3.1",
                "markdown": False,
                "stream": False
            }

            try:
                if stream != None and stream == True:
                    strm = True
                else:
                    strm = False
            except Exception as e:
                strm = False
            
            try:
                data = {
                    "messages": messages if messages is not None else [],
                    "markdown": markdown if markdown is not None else False,
                    "stream": strm if strm is not None else False,
                    "model": "llama-3.1"
                }
            except Exception as e:
                data = {
                    "messages": [],
                    "model": "llama-3.1",
                    "markdown": False,
                    "stream": False
                }

            try:
                res_ = apistrm(data=data, api="https://nexra.aryahcr.cc/api/chat/complements", stream=strm)
                self.__error = res_.error()
                self.__result = res_.result()
                self.__sttrm = res_.stream()
            except Exception as e:
                self.__error = {
                    "code": 500,
                    "status": False,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }
                self.__result = None
        except Exception as e:
            self.__error = {
                "code": 500,
                "status": False,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__result = None
            self.__sttrm = None
        pass
    def stream(self):
        if self.__sttrm != None:
            for data in self.__sttrm:
                yield data
        else:
            yield None
    def error(self):
        return self.__error
    def result(self):
        return self.__result
