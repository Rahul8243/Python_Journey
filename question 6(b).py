def friends_in_trouble(j_angry, s_angry):
    if j_angry and s_angry:
        return True
    elif not j_angry and not s_angry:
        return True
    else:
        return False
    
print(friends_in_trouble(True, True))
print(friends_in_trouble(True, False))
print(friends_in_trouble(False, False))