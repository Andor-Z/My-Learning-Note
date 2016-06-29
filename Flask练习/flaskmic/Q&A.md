#[Flask Mega Tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html)

## **Q:**forms.py 中的表单类表单属性的验证器validators=[]中`Required()``DataRquired()`的区别？


## **Q:**Flask表单的几种使用方法
1. 
`{% import "bootstrap/wtf.html" as wtf %}`  
    `{{ wtf.quick_form(form) }}`

2.

```
    <form action="" method="post" name="login">
        {{ form.hidden_tage() }} 
        {# form.hidden_tag() 模板参数将被替换为一个隐藏字段，用来是实现在配置中激活的 CSRF 保护。如果你已经激活了 CSRF，这个字段需要出现在你所有的表单中。 #}
        <p>
            Please enter your OpenID:<br>
            {{ form.openid(size = 80) }}<br>
        </p>
        <p>{{ form.remember_me }}Remember Me</p>
        <p><input type="submit" value="Sign In"></input></p>
    </form>
```
## **Q:**`flash`的表示方法
1.
```
    {% for message in get_flashed_messages() %}
    
        {{ message }}
    {% endfor %}
```

2.
```
    {% with messages = get_flashed_messages() %}
    {% if messages %}
    <ul>
    {% for message in messages %}
        <li>{{ message }} </li>
    {% endfor %}
    </ul>
    {% endif %}
    {% endwith %}
```