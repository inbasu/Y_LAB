## Y_LAB
### Fast API project.
**v1**

TEST:
![Снимок экрана от 2023-07-23 14-28-30](https://github.com/inbasu/Y_LAB/assets/13472561/0701ac1c-3669-48d2-b352-7339586a5f69)

#### Alchemy
**Menus**
- title
- description
- count of submenu (hybrid property)
- count of dishes in submenus (hybrid property)
- relatonship to SubMenu

**SubMenus**
- title
- description
- many to one with Menus (forei:w
- nkey)
- count of dishes (hybrid property)
- relatonship to Dishes

**Dished**
- title
- description
- price
- many to one with SubMenus (foreinkey)


ps. Thanks to Y_LAB for good practice. This is my first FastAPI project.
pps. Test was launched in postman and model id in test chech eql as string, thats why I conver model id from int to string manuly.
