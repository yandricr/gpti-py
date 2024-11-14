import requests
import json
import time
from urllib.parse import quote

_cred = {
    "x-nexra-user": None,
    "x-nexra-secret": None
}

def nexra(user, secret):
    global _cred
    try:
        _cred["x-nexra-secret"] = secret if type(secret) is str else None
        _cred["x-nexra-user"] = user if type(user) is str else None
    except Exception as e:
        _cred["x-nexra-secret"] = None
        _cred["x-nexra-user"] = None

class api:
    def __init__(self, data={}, api="", image=False):
        global _cred

        try:
            data_ = None
            try:
                data_ = json.dumps(data)
                data_ = json.loads(data_)
            except Exception as e:
                raise "err"
            
            head_ = {
                "Content-Type": "application/json"
            }
            head_.update(_cred)

            data_ = json.dumps(data_)
            req = requests.post(url=api, data=data_, headers=head_)

            if req.status_code == 200:
                api_url = "https://nexra.aryahcr.cc/api/chat/task/"
                try:
                    if image is not None and image == True:
                        api_url = "http://nexra.aryahcr.cc/api/image/complements/"
                    else:
                        raise("Error")
                except Exception as e:
                    api_url = "https://nexra.aryahcr.cc/api/chat/task/"

                response = req.json()
                id = response.get("id")

                check_data = True
                data_ = None
                error_ = None
                while(check_data):
                    time.sleep(1)
                    try:
                        response = requests.get(api_url + quote(id))
                        if response.status_code == 200:
                            response = response.json()

                            match response.get("status"):
                                case "pending":
                                    check_data: True
                                case "completed":
                                    data_ = response
                                    check_data = False
                                    break
                                case "error" | "not_found" | _:
                                    error_ = response
                                    check_data = False
                        else:
                            raise("Error")
                    except Exception as e:
                        check_data = False
                        error_ = None
                        data_ = None
                
                if data_ != None:
                    self.__res = data_
                    self.__err = None
                elif error_ != None:
                    self.__res = None
                    self.__err = error_
                else:
                    raise("error")
            else:
                data_err = {
                    "code": 500,
                    "error": "INTERNAL_SERVER_ERROR",
                    "message": "general (unknown) error"
                }

                try:
                    data_err = req.json()
                except Exception as e:
                    data_err = {
                        "code": 500,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }

                self.__err = data_err
                self.__res = None
        except Exception as e:
            self.__err = {
                "code": 500,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__res = None
        pass
    def result(self):
        return self.__res
    def error(self):
        return self.__err

class apistrm:
    def __init__(self, data={}, api="", stream=False):
        global _cred

        try:
            data_ = None
            try:
                data_ = json.dumps(data)
                data_ = json.loads(data_)
            except Exception as e:
                raise "err"
            
            head_ = {
                "Content-Type": "application/json"
            }
            head_.update(_cred)

            data_ = json.dumps(data_)

            strm_ = False
            try:
                if type(stream) is bool and stream == True:
                    strm_ = True
                else:
                    strm_ = False
            except Exception as e:
                strm_ = False

            if strm_ != True:
                self.__strm = None
                req = requests.post(url=api, data=data_, headers=head_)

                if req.status_code == 200:
                    response = req.json()
                    id = response.get("id")

                    check_data = True
                    data_ = None
                    error_ = None
                    while(check_data):
                        time.sleep(1)
                        try:
                            response = requests.get("https://nexra.aryahcr.cc/api/chat/task/" + quote(id))
                            if response.status_code == 200:
                                response = response.json()

                                match response.get("status"):
                                    case "pending":
                                        check_data: True
                                    case "completed":
                                        data_ = response
                                        check_data = False
                                        break
                                    case "error" | "not_found" | _:
                                        error_ = response
                                        check_data = False
                            else:
                                raise("Error")
                        except Exception as e:
                            check_data = False
                            error_ = None
                            data_ = False
                    
                    if data_ != None:
                        self.__res = data_
                        self.__err = None
                    elif error_ != None:
                        self.__res = None
                        self.__err = error_
                    else:
                        raise("error")
                else:
                    data_err = {
                        "code": 500,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    
                    try:
                        data_err = req.json()
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }

                    self.__err = data_err
                    self.__res = None
            else:
                req = requests.post(url=api, data=data_, headers=head_, stream=True)

                if req.status_code == 200:
                    self.__strm = req
                    self.__err = None
                    self.__res = None
                else:
                    data_err = {
                        "code": 500,
                        "error": "INTERNAL_SERVER_ERROR",
                        "message": "general (unknown) error"
                    }
                    
                    try:
                        data_err = req.json()
                    except Exception as e:
                        data_err = {
                            "code": 500,
                            "error": "INTERNAL_SERVER_ERROR",
                            "message": "general (unknown) error"
                        }

                    self.__err = data_err
                    self.__res = None
                    self.__strm = None
        except Exception as e:
            self.__strm = None
            self.__err = {
                "code": 500,
                "error": "INTERNAL_SERVER_ERROR",
                "message": "general (unknown) error"
            }
            self.__res = None
        pass
    def result(self):
        return self.__res
    def error(self):
        return self.__err
    def stream(self):
        if self.__strm != None:
            try:
                tmp = None
                err = None
                for chunk in self.__strm.iter_lines(chunk_size=1024):
                    if err == None:
                        if chunk:
                            chk = chunk.decode()
                            chk = chk.split("")

                            for data in chk:
                                result = None

                                try:
                                    convert = json.loads(data)
                                    result = data
                                    tmp = None
                                except Exception as e:
                                    if tmp == None:
                                        tmp = data
                                    else:
                                        try:
                                            convert = json.loads(tmp)
                                            result = tmp
                                            tmp = None
                                        except Exception as e:
                                            tmp = tmp + data
                                            try:
                                                convert = json.loads(tmp)
                                                result = tmp
                                                tmp = None
                                            except Exception as e:
                                                tmp = tmp
                                
                                if result != None:
                                    try:
                                        result = json.loads(result)
                                        if result.get("code") == None and result.get(
                                            "status") == None:
                                            yield result
                                        else:
                                            err = result
                                            yield err
                                    except Exception as e:
                                        pass
            except Exception as e:
                yield {"message":None,"original":None,"finish":True,"error":True}
        else:
            yield None
        pass
