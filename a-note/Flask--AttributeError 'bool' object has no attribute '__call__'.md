2016年3月1日

在学习Flask-Login模块时，出现了报错`builtins.AttributeError AttributeError: 'bool' object has no attribute '__call__'`。
**参考资料**：[When I run app.py, why am I getting: builtins.AttributeError AttributeError: 'bool' object has no attribute '__call__'](https://teamtreehouse.com/community/when-i-run-apppy-why-am-i-getting-builtinsattributeerror-attributeerror-bool-object-has-no-attribute-call)

> **Kenneth Love**：Posting this here so people can see it, this comes from a change in how UserMixin works in flask-login. I'd tell you to install a specific version of flask-login but...they removed those releases from PyPI.

> So...instead of {{ current_user.is_authenticated() }}, you need to use {{ current_user.is_authenticated }}. Just don't include the parentheses. Yeah, it's an annoying change but, honestly, I think it's probably better code design.

**原因**：flask-login 模块里的`UserMixin`类由于版本更新后，修改了它的`is_authenticated()` 方法，在之前的版本中是使用`UserMixin.is_authenticated()` 根据用户已经登录返回`True`，未登录返回`False`，而现在改成使用`UserMixin.is_authenticated` 了。上文中的Kenneth Love表示虽然这是个烦人的改变，但他认为这是一种更好的代码设计。

**解决办法**：去掉`is_authenticated()`中的括号。