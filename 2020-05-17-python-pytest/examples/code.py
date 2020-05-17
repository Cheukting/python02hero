def serve_beer(age):
    if age is None:
        raise(ValueError("Tell me your age"))
    if age<18:
      return "No beer"
    else:
      return "Have beer"
