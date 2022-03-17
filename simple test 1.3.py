def uploadImg(request, dir_name="static/upload"):
    ##################
    #  kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("img")
    if files:
        result =image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")