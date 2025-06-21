from flet import * 
def main(apk:Page):
          apk.window.height=740
          apk.window.width=390
          apk.window.left=990
          apk.window.top=10
          apk.theme_mode=ThemeMode.LIGHT
          

          def route_change(route):
                 # page 1 
                  apk.views.clear()
                  apk.views.append(
                          View(
                                  '/',
                                  [
                                          AppBar(
                                                  title=Text('ghaith flet'),
                                                  color=colors.WHITE,
                                                  bgcolor=colors.PURPLE,
                                          ),
                                          Text('Welcom ....',size=24,color=colors.BLACK,width=370,text_align='center'),
                                          Row([
                                             Image(src='login.gif',width=280)     
                                          ],alignment=MainAxisAlignment.CENTER),
                                          Text('اهلا وسهلا في تطبيقنا',size=15,color=colors.PURPLE,width=370,text_align='center',weight=FontWeight.BOLD),
                                          Row([
                                                  ElevatedButton(
                                                          'دخول الحساب\nlogin page',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          on_click=lambda _: apk.go('/login')
                                                  ),
                                                 
                                                   ElevatedButton(
                                                          ' انشاء حساب\nsignup page',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          on_click=lambda _: apk.go('/signup page')
                                                  ),
                                          ],alignment=MainAxisAlignment.CENTER),
                                  
                                    
                                  
                                  ]
                                  )
                  )
                  #page2
                  if apk.route=='/login':
                          apk.views.append(
                          View(
                                  '/',
                                  [
                                   AppBar(
                                          title=Text('login system'),
                                          color=colors.WHITE,
                                          bgcolor=colors.PURPLE,
                                  ),
                                  Text('تسجيل دخول ',size=24,color=colors.BLACK,width=370,text_align='center',weight=FontWeight.BOLD),
                                  TextField(label='Email',icon=icons.EMAIL),       
                                  TextField(label='password',icon=icons.PASSWORD,password=True,can_reveal_password=True),
                                   Row([
                                                  ElevatedButton(
                                                          'دخول الان',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          
                                                  ),
                                                 
                                                   ElevatedButton(
                                                          ' انشاء حساب جديد',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          on_click=lambda _: apk.go('/signup page')
                                                  ),
                                          ],alignment=MainAxisAlignment.CENTER),
                                         
                                  
                                  ]
                                  )
                  )
                  # page3        
                  if apk.route=='/signup page':
                           apk.views.append(
                          View(
                                  '/',
                                  [
                                   AppBar(
                                          title=Text('signup system'),
                                          color=colors.WHITE,
                                          bgcolor=colors.PURPLE,
                                  ),
                                  Text('انشاء حساب جديد ',size=24,color=colors.BLACK,width=370,text_align='center',weight=FontWeight.BOLD),
                                   TextField(label='Email:الحساب',icon=icons.EMAIL),        
                                   TextField(label='full name:الاسم الكامل',icon=icons.NEAR_ME_DISABLED),        
                                   TextField(label='password:كلمة المرور',icon=icons.PASSWORD,password=True,can_reveal_password=True),        
                                   TextField(label='repassword:اعادة كلمة المرور',icon=icons.PASSWORD,password=True,can_reveal_password=True),
                                   Row([
                                                  ElevatedButton(
                                                          ' انشاء حساب',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          
                                                  ),
                                                 
                                                   ElevatedButton(
                                                          '  لديك حساب بالفعل ',
                                                          width=170,
                                                          style=ButtonStyle(bgcolor=colors.PURPLE,color=colors.WHITE),
                                                          on_click=lambda _: apk.go('/login')
                                                  ),
                                          ],alignment=MainAxisAlignment.CENTER),        
                                  
                                  ]
                                  )
                  )        
                  
         
          
          
                  apk.update()
          
          def page_go(view):
                  apk.views.pop()
                  back_page=apk.views[-1]
                  apk.go(back_page.route)
          
          apk.on_route_change= route_change
          apk.on_view_pop=page_go
          apk.go(apk.route)



app(main)