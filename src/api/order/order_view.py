# from typing import Annotated
# from fastapi import APIRouter, Depends, Request, Form, status, Path
# from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates
 
# from sqlalchemy.orm import Session
 
# from api.order import models
# from core.models import db_helpr as get_db
# from pathlib import Path
# from api.order.schema import Order


 
# BASE_DIR = Path(__file__).resolve().parent
# # templates = Jinja2Templates(directory="templates")
# templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
 
# router = APIRouter(prefix="/order", tags=["Orders"])


# @router.get("/")
# def home(request: Request, db: Session = Depends(get_db)):
#     orders = db.query(models.Order).filter(models.Order.curent_section == "admin").all()
#     return templates.TemplateResponse(name="index.html",
#                                       request=request, context={"orders_list": orders, 'title': "Admin Section"})


# @router.post("/add")
# def add(request: Request, order: Order = Form(...), db: Session = Depends(get_db)):
#     print(order.title)
#     new_order = models.Order(
#         outside_number = order.outside_number,
#         title = order.title,
#         description = order.description,
#         type = order.type,
#         gem = order.gem,
#         metal = order.metal,
#         curent_section = "admin"
#     )
#     db.add(new_order)
#     db.commit()
 
#     url = router.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
 

# @router.put("/update/{order_id}")
# def update(request: Request, order_id: Annotated[int, Path(gt=1, lt=10000)], order: Order, db: Session = Depends(get_db)):
#     update_order = db.query(models.Order).filter(models.Order.id == order_id).first()
#     db.add(update_order)
#     db.commit()
#     return templates.TemplateResponse(name="update.html",
#                                       request=request, context={"order": order})


# @router.get("/next/{order_id}")
# def next(request: Request, order_id: Annotated[int, Path(gt=1, lt=10000)], db: Session = Depends(get_db)):
#     order = db.query(models.Order).filter(models.Order.id == order_id).first()
#     if order.curent_section == 'admin':
#         order.curent_section = 'designer'
#     elif order.curent_section == 'designer':
#         order.curent_section = 'jule'
#     elif order.curent_section == 'jule':
#         order.curent_section = 'setter'
#     elif order.curent_section == 'setter':
#         order.curent_section = 'dane'

#     db.commit()
 
#     url = router.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
 

# @router.get("/back/{order_id}")
# def back(request: Request, order_id: Annotated[int, Path(gt=1, lt=10000)], db: Session = Depends(get_db)):
#     order = db.query(models.Order).filter(models.Order.id == order_id).first()
#     if order.curent_section == 'done':
#         order.curent_section = 'setter'
#     elif order.curent_section == 'setter':
#         order.curent_section = 'jule'
#     elif order.curent_section == 'jule':
#         order.curent_section = 'designer'
#     elif order.curent_section == 'designer':
#         order.curent_section = 'admin'

#     db.commit()
 
#     url = router.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
 
# @router.get("/delete/{order_id}")
# def delete(request: Request, order_id: Annotated[int, Path(gt=1, lt=10000)], db: Session = Depends(get_db)):
#     order_id = db.query(models.Order).filter(models.Order.id == order_id).first()
#     db.delete(order_id)
#     db.commit()
 
#     url = router.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


# @router.get("/designer")
# def designer(request: Request, db: Session = Depends(get_db)):
#     orders = db.query(models.Order).filter(models.Order.curent_section == 'designer').all()
#     return templates.TemplateResponse(name="designer.html",
#                                       request=request, context={"orders_list": orders, 'title': "Designer Section"})
 