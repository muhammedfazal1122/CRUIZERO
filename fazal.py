from flask import *
from Dbconnection import *
app = Flask(__name__)
app.secret_key="1234567890"

@app.route('/')
def login():
    return render_template("admin/login page admin.html")

@app.route("/login_post", methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="SELECT * FROM login WHERE username = '"+username+"' AND PASSWORD = '"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        if res['type']=="admin":
            session['lid']=res['login_id']
            return redirect('/admin_home_page')
        elif res['type']=="ship":
            session['lid']=res['login_id']
            return redirect('/ship_home_page')
        elif res['type']=="staff":
            session['lid']=res['login_id']

            return redirect('/staff_home_page')
        elif res['type']=="user":
            session['lid']=res['login_id']

            return redirect('/admin_home_page')
        else:
            return '''<script>alert('User not Found');wndow.location="/"</script>'''
    else:
        return '''<script>alert('User not Found');wndow.location="/"</script>'''






@app.route("/admin_home_page")
def admin_home_page():
    return render_template("admin/admin home page.html")






@app.route("/admin_edit_ship/<sid>")
def admin_edit_ship(sid):
    db=Db()
    qry="select * from ship where ship_id='"+sid+"'"
    res=db.selectOne(qry)
    return render_template("admin/edit ship.html",data=res)







@app.route("/admin_edit_ship_post",methods=['post'])
def admin_edit_ship_post():
    id=request.form['sid']
    ship_name=request.form['textfield2']
    discription=request.form['textarea']
    capacity=request.form['textfield3']
    if 'fileField' in request.files:
        photo = request.files['fileField']
        if photo.filename!="":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d-%H%M%S")
            photo.save("C:\\Users\\user\\PycharmProjects\\cruize in my hand\\static\\shipimage\\" + date + ".jpg")
            path = "/static/shipimage/" + date + ".jpg"
            db = Db()
            qry = "UPDATE ship SET ship_name='" + ship_name + "',discription='" + discription + "',photo='" + path + "',capacity='" + capacity + "' Where ship_id='" + str(id) + "' "
            res = db.update(qry)
            return "<script>alert('updated');window.location='/admin_view_ship'</script>"
        else:
            db = Db()
            qry = "UPDATE ship SET ship_name='" + ship_name + "',discription='" + discription + "',capacity='" + capacity + "' Where ship_id='" + str(id) + "'"
            res = db.update(qry)
            return "<script>alert('updated');window.location='/admin_view_ship'</script>"
    else:
        db = Db()
        qry = "UPDATE ship SET ship_name='" + ship_name + "',discription='" + discription + "',capacity='" + capacity + "' Where ship_id='" + str(id) + "' "
        res = db.update(qry)
        return "<script>alert('updated');window.location='/admin_view_ship'</script>"



@app.route("/admin_delete_ship/<sid>")
def admin_delete_ship(sid):
    db=Db()
    qry="delete from ship where ship_id='"+str(sid)+"'"
    res=db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/admin_view_ship"</script>'''






@app.route("/admin_facilities")
def admin_facilities():
    qry="select * from ship"
    db=Db()
    res=db.select(qry)
    return render_template("admin/facilities.html",data=res)


@app.route("/facilities_post",methods=['post'])
def facilities():
    ship=request.form['textfield']
    facilities=request.form["textfield2"]
    description=request.form['textarea']
    charge=request.form['textfield3']
    db=Db()
    qry="INSERT INTO facilities VALUES('',''"+ship+"','"+facilities+",'"+description+"','"+charge+"')"
    return "ok"









@app.route("/admin_manage_journy")
def admin_manage_journy():
    db=Db()
    qry="select * from ship"
    res=db.select(qry)
    return render_template("admin/manage journy.html",data=res)


@app.route("/manage_journy",methods=['post'])
def manage_journy():
    ship=request.form['select']
    departure=request.form['textfield2']
    arrival=request.form['textfield3']
    start_date=request.form['textfield4']
    end_date=request.form['textfield5']
    status=request.form['textfield6']
    db=Db()
    qry="INSERT INTO journey VALUES('','"+ship+"','"+departure+"','"+arrival+"','"+start_date+"','"+end_date+"','"+status+"')"
    res=db.insert(qry)
    return "ok"










@app.route("/admin_port")
def admin_port():
    return render_template("admin/port.html")


@app.route("/port", methods=['post'])
def port():
    port_name=request.form['textfield']
    country_name=request.form['select']
    country_code=request.form['textfield2']
    longitude=request.form['textfield3']
    latitude=request.form['textfield4']
    db=Db()
    qry="INSERT INTO PORT VALUES('','"+port_name+"','"+country_name+"','"+country_code+"','"+longitude+"','"+latitude+"')"
    res=db.insert(qry)

    return "ok"




@app.route("/admin_reply")
def admin_reply():
    return render_template("admin/reply.html")


@app.route("/replyt", methods=['post'])
def reply():
    reply=request.form['textarea']
    return  "ok"










@app.route("/admin_ship_add")
def admin_ship_add():


    return render_template("admin/ship add.html")

@app.route("/ship_add",methods=['post'])
def ship_add():
    ship_name=request.form['textfield2']
    description=request.form['textarea']
    from datetime import datetime
    photo=request.files['fileField']
    date=datetime.now().strftime("%Y%m%d-%H%M%S")
    photo.save("C:\\Users\\user\\PycharmProjects\\cruize in my hand\\static\\shipimage\\"+date+".jpg")
    path="/static/shipimage/"+date+".jpg"
    capacity=request.form['textfield3']
    import random
    password=random.randint(0000,9999)
    db=Db()
    # qry1 = "insert into login(`username`,`password`,`type`) values ('" + ship_name + "','" + str(password) + "','ship')"
    # res1 = db.insert(qry1)
    qry2="INSERT INTO `ship`(`login_id`,`ship_name`,`discription`,`capacity`,`photo`)VALUES('1','"+ship_name+"','"+description+"','"+capacity+"','"+path+"')"
    res2=db.insert(qry2)

    return "ok"










@app.route("/admin_view_complaint")
def admin_view_complaint():
    db=Db()
    qry="SELECT * FROM complaint,USER WHERE complaint.ul_id=user.login_id;"
    res=db.select(qry)
    return render_template("admin/view complaint.html",data=res)







@app.route("/admin_view_facilities")
def admin_view_faciities():
    db=Db()
    qry="SELECT * FROM facilities ,ship WHERE facilities.ship_id=ship.ship_id"
    res=db.select(qry)
    print(res)
    return render_template("admin/view facilities.html",data=res)

@app.route("/admin_delete_facilities/<fid>")
def admin_delete_facilities(fid):
    db = Db()
    qry = "delete from facilities where f_id='" + str(fid) + "'"
    res = db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/admin_view_facilities"</script>'''


@app.route("/admin_edit_facilities/<fid>")
def admin_edit_facilities(fid):
    db=Db()
    qry="SELECT * FROM facilities ,ship WHERE facilities.ship_id=ship.login_id and  facilities.f_id='"+fid+"'"
    res=db.selectOne(qry)
    q1 ="SELECT * FROM `ship`"
    r1 = db.select(q1)
    return render_template("admin/edit_facilities.html",data=res,data1=r1)


@app.route("/admin_edit_facilities_post",methods=['post'])
def admin_edit_facilities_post():
    id = request.form['fid']
    ship=request.form['textfield']
    facilities=request.form['textfield2']
    discription=request.form['textarea']
    charge=request.form['textfield3']
    db=Db()
    qry="UPDATE facilities SET f_id='"+id+"',ship_id='"+ship+"',facility='"+facilities+"',`description`='"+discription+"',charge='"+charge+"' Where f_id='"+str(id)+"' "
    res=db.update(qry)
    print(res)
    return redirect('/admin_view_facilities')





@app.route("/admin_view_journey")
def admin_view_journey():

    db=Db()
    qry="SELECT * FROM journey, ship WHERE journey.ship_id=ship.ship_id"
    res=db.select(qry)
    return render_template("admin/view journey.html",data=res)

@app.route("/admin_delete_journey/<jid>")
def admin_delete_journey(jid):
    db = Db()
    qry = "delete from journey where journey_id='" + str(jid) + "'"
    res = db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/admin_view_journey"</script>'''


@app.route("/admin_edit_journey/<jid>")
def admin_edit_journey(jid):
    db=Db()
    qry="select * from journey where journey_id='"+jid+"'"
    res=db.selectOne(qry)
    qry1="select * from ship"
    res1=db.select(qry1)
    return render_template("admin/edit_journy.html",data=res,data1=res1)


@app.route('/edit_journey_post',methods=['post'])
def edit_journey_post():
    jid=request.form['j_id']
    ship=request.form['select']
    departure=request.form['textfield2']
    arrival=request.form['textfield3']
    start_date=request.form['textfield4']
    end_date=request.form['textfield5']
    status=request.form['textfield6']
    db=Db()
    qry="UPDATE journey SET journey_id='"+jid+"',ship_id='"+ship+"',start_port='"+departure+"',end_port='"+arrival+"',start_date='"+start_date+"',end_date='"+end_date+"',status='"+status+"' Where journey_id='"+str(jid)+"'  "
    res=db.insert(qry)
    return "ok"










@app.route("/admin_view_port")
def admin_view_port():
    db=Db()
    qry="SELECT * FROM PORT;"
    res=db.select(qry)
    return render_template("admin/view port.html",data=res)

@app.route("/admin_delete_port/<pid>")
def admin_delete_port(pid):
    db=Db()
    qry="delete from port where port_id='"+str(pid)+"'"
    res=db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/admin_view_port"</script>'''


@app.route("/admin_edit_port/<pid>")
def admin_edit_port(pid):
    db=Db()
    qry="select * from port where port_id='"+pid+"'"
    res=db.selectOne(qry)
    return render_template("admin/edit_port.html",data=res)


@app.route("/admin_edit_port_post",methods=['post'])
def admin_edit_port_post():
    id = request.form['pid']
    port_name=request.form['textfield']
    country_name=request.form['select']
    country_code=request.form['textfield2']
    longitude=request.form['textfield3']
    latitude=request.form['textfield4']
    db=Db()
    qry="UPDATE PORT SET port_name='"+port_name+"',country_name='"+country_name+"',country_code='"+country_code+"',longitude='"+longitude+"',latitude='"+latitude+"' Where port_id='"+str(id)+"' "
    res=db.update(qry)
    print(res)
    return admin_view_port()




@app.route("/admin_view_reply")
def admin_view_reply():
    return render_template("admin/view reply.html")






@app.route("/admin_sent_reply/<complaint_id>")
def admin_sent_reply(complaint_id):
    db=Db()
    qry="SELECT * FROM complaint WHERE complaint_id='"+complaint_id+"'"
    res=db.selectOne(qry)
    return render_template("admin/sent reply.html",data=res)


@app.route("/admin_sent_reply_post",methods=['post'])
def admin_sent_reply_post():
    reply=request.form['textarea']
    cid=request.form['cid']
    qry="UPDATE `complaint` SET reply='"+reply+"',`status`='replied' WHERE complaint_id='"+cid+"' "
    db = Db()
    res=db.update(qry)
    return redirect('/admin_view_complaint')

@app.route("/admin_view_ship")
def admin_view_ship():
    db=Db()
    qry="select * from ship"
    res=db.select(qry)
    return render_template("admin/view ship.html",data=res)


@app.route("/g")
def g():
    return render_template("admin/shipblog.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
















# %%%%%%%%%*******************!!!!!!!!!!!!!!!!!!!!ship----------$$$$$$$$$$$$$########################################################################







@app.route("/ship_home_page")
def ship_home_page():
    return render_template("ship/ship_home_page.html")





@app.route("/ship_manage_facilities")
def ship_manage_facilities():
    return render_template("ship/manage facilities.html")


@app.route("/ship_manage_facilities_post",methods=['post'])
def ship_manage_facilities_post():
    facilities=request.form['textfield2']
    description=request.form['textarea']
    charge=request.form['textfield3']
    db=Db()
    qry="insert into facilities(ship_id,facilities,description,charge) values('"+str(session['lid'])+"','"+facilities+"','"+description+"','"+charge+"')"
    res=db.insert(qry)
    print(res)
    return "ok"





@app.route("/ship_allocate_work/<wid>")
def ship_altlocate_work(wid):
    db=Db()
    qry="select * from staff"
    res=db.select(qry)
    qry1="select * from work where work_id='"+wid+"' "
    res1=db.selectOne(qry1)
    return render_template("ship/allocate work.html",data=res,data1=res1)



@app.route("/ship_allocate_work_post",methods=['post'])
def ship_allocate_work_post():
    db=Db()
    id=request.form['wid']
    staff=request.form['select']
    qry="insert into `allocate work` (staff_id,work_id,status) values ('"+staff+"','"+id+"','pending')"
    res=db.insert(qry)
    qry1="update work set status='allocated' where work_id='"+id+"' "
    res1=db.update(qry1)
    return "ok"




@app.route("/ship_view_schedule")
def ship_view_schedule():
    db = Db()
    qry = "SELECT * FROM SCHEDULE WHERE ship_id='"+str(session['lid'])+"'"
    res = db.select(qry)
    return render_template("ship/view schedule.html",data=res)




@app.route("/ship_view_work_activities")
def ship_view_work_activities():
    db=Db()
    qry="SELECT* FROM WORK JOIN `allocate work` ON `allocate work`.work_id=work.work_id JOIN staff ON staff.login_id=`allocate work`.staff_id JOIN `activities in work` ON work.work_id=`activities in work`.work_id GROUP BY `allocate work`.staff_id"
    res=db.select(qry)

    return render_template("ship/view work activities.html",data=res)



@app.route("/ship_staff_management")
def ship_staff_management():
    db=Db()
    return render_template("ship/staff management.html")

@app.route("/ship_staff_management_post",methods=['post'])
def ship_staff_management_post():
    staff_name=request.form['textfield2']
    place=request.form['textfield']
    email=request.form['textfield4']
    phone=request.form['textfield5']
    pin=request.form['textfield6']
    work=request.form['textfield3']
    db=Db()
    qry1="insert into login(`username`,`password`,`type`) values ('"+email+"','"+phone+"','staff')"
    res1=db.insert(qry1)

    qry="INSERT INTO`staff`(ship_id,login_id,`name`,`place`,`pin`,`email`,`phone`,`work`) VALUES('"+str(session['lid'])+"','"+str(res1)+"','"+staff_name+"','"+place+"','"+pin+"','"+email+"','"+phone+"','"+work+"')"
    db=Db()
    res=db.insert(qry)
    return "ok"


@app.route("/ship_view_staff_management")
def ship_view_staff_management():
    db=Db()
    qry="select * from staff"
    res=db.select(qry)

    return render_template("ship/view staff management.html",data=res)




@app.route("/ship_delete_staff_management/<sid>")
def ship_delete_staff_management(sid):
    db=Db()
    qry="delete from staff where staff_id='"+str(sid)+"'"
    res=db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/ship_view_staff_management"</script>'''





@app.route("/ship_edit_staff_management/<sid>")
def ship_edit_staff_management(sid):
    db=Db()
    qry="select * from staff where staff_id='"+sid+"'"
    res=db.selectOne(qry)
    return render_template("ship/editstaff.html",data=res)


@app.route("/ship_edit_staff_management_post",methods=['post'])
def ship_edit_staff_management_post():
    id = request.form['sid']
    staff_name=request.form['textfield2']
    place=request.form['textfield']
    pin=request.form['textfield6']
    email=request.form['textfield4']
    phone=request.form['textfield5']
    work= request.form['textfield3']
    db=Db()
    qry="UPDATE staff SET name='"+staff_name+"',place='"+place+"',pin='"+pin+"',email='"+email+"',phone='"+phone+"',work='"+work+"' Where staff_id='"+str(id)+"' "
    res=db.update(qry)
    print(res)
    return ship_view_staff_management()




@app.route("/ship_work_management")
def ship_work_management():
    db=Db()
    return render_template("ship/work_management.html")




@app.route("/ship_work_management_post",methods=['post'])
def ship_work_management_post():
    work=request.form['textfield']
    date=request.form['textfield2']
    qry="INSERT INTO WORK (ship_id,work,date,status)VALUES('"+str(session['lid'])+"','"+work+"','"+date+"','pending')"
    db=Db()
    res=db.insert(qry)
    return "ok"






@app.route("/ship_view_work_management")
def ship_view_work_management():
    db=Db()
    qry="select * from work"
    # qry="SELECT* FROM WORK JOIN `allocate work` ON `allocate work`.work_id=work.work_id JOIN staff ON staff.login_id=`allocate work`.staff_id"
    res=db.select(qry)
    return render_template("ship/view work management.html",data=res)








@app.route("/ship_delete_work_management/<wid>")
def ship_delete_work_management(wid):
    db=Db()
    qry="delete from work where work_id='"+str(wid)+"'"
    res=db.delete(qry)
    return '''<script>alert('delete successfully');window.location="/ship_view_work_management"</script>'''





@app.route("/ship_edit_work_management/<wid>")
def ship_edit_work_management(wid):
    db=Db()
    qry="select * from work where work_id='"+wid+"'"
    res=db.selectOne(qry)
    return render_template("ship/edit work management.html",data=res)


@app.route("/ship_edit_work_management_post",methods=['post'])
def ship_edit_work_management_post():
    id = request.form['wid']
    work=request.form['textfield']
    date=request.form['textfield2']
    db=Db()
    qry="UPDATE work SET work='"+work+"',date='"+date+"' where work_id='"+id+"' "
    res=db.update(qry)
    print(res)
    return "<script>alert('Work updated');window.location='/ship_view_work_management'</script>"



@app.route("/ship_view_accept_reject_booking")
def ship_view_accept_reject_booking():
    db=Db()
    qry="select * from booking inner join user on user.login_id=booking.login_id where status = 'pending'"
    res=db.select(qry)
    return render_template("ship/accept_reject_booking.html",data=res)




@app.route("/ship_acceptedbooking")
def ship_acceptedbooking():
    db=Db()
    qry="select * from booking inner join user on user.login_id=booking.login_id where status = 'approved'"
    res=db.select(qry)
    return render_template("ship/acceptedbooking.html",data=res)



@app.route("/ship_rejectedbooking")
def ship_rejectedbooking():
    db=Db()
    qry="select * from booking inner join user on user.login_id=booking.login_id where status = 'rejected'"
    res=db.select(qry)
    return render_template("ship/rejectedbooking.html",data=res)










@app.route('/ship_accept_booking/<id>')
def ship_accept_booking(id):
    db = Db()
    qry = "update booking set status = 'approved' where booking_id = '"+id+"'"
    res = db.update(qry)
    return redirect('/ship_view_accept_reject_booking')



@app.route('/ship_reject_booking/<id>')
def ship_reject_booking(id):
    db=Db()
    qry="update booking set status = 'rejected' where booking_id='"+id+"'"
    res=db.update(qry)
    return redirect ('/ship_view_accept_reject_booking')


















@app.route("/ship_view_work_status")
def ship_view_work_status():
    db=Db()
    qry="select * from work inner join `allocate work` on work.work_id=`allocate work`.work_id inner join staff on staff.login_id=`allocate work`.staff_id  "
    res=db.select(qry)
    return render_template("ship/view work status.html",data=res)

@app.route("/ship_work")
def ship_work():
    return render_template("ship/work.html")




@app.route("/view_user_onboard")
def view_user_onboard():
    db=Db()
    qry="SELECT* FROM USER JOIN booking ON booking.login_id=user.login_id WHERE booking.status='approved' AND ship_id='"+str(session['lid'])+"'"
    print(qry)
    res=db.select(qry)
    return render_template("ship/view user onboard.html",data=res)


@app.route('/allocate_room')
def allocate_room():
    qry="SELECT *FROM room WHERE ship_id='"+str(session['lid'])+"' "
    db = Db()
    res1=db.select(qry)
    qry1="SELECT * FROM USER JOIN booking ON booking.login_id=user.login_id WHERE booking.status='approved' AND ship_id='"+str(session['lid'])+"'"
    db = Db()
    res2=db.select(qry1)
    return render_template("ship/allocate room.html",data1=res1,data2=res2)



@app.route("/ship_allocate_room", methods=['POST'])
def ship_allocate_room():
    room=request.form['select']
    user=request.form['select2']
    qry = "SELECT * FROM `allocate room` WHERE `room_id`='"+room+"' OR `user_id`='"+user+"'"
    db=Db()
    res=db.selectOne(qry)
    if res is None:

        qry="INSERT INTO `allocate room` (room_id,user_id) VALUES ('"+room+"','"+user+"')"
        db = Db()
        db.insert(qry)
        return "<script>alert('assigned');window.location='/allocate_room'</script>"
    else:
        return "<script>alert('already assigned');window.location='/allocate_room'</script>"





@app.route('/ship_view_allocated_room')
def ship_view_allocated_room():
    db=Db()
    qry="SELECT * FROM `allocate room` INNER JOIN `room` ON `allocate room`.`room_id`=`room`.`room_id` INNER JOIN `user` ON user.`login_id`=`allocate room`.user_id"
    res=db.select(qry)
    return render_template("ship/view allocated room.html",data=res)


@app.route('/ship_view_rating')
def ship_view_rating():
    db=Db()
    qry="SELECT* FROM USER INNER JOIN rating ON rating.user_id=user.login_id WHERE ship_id='"+str(session['lid'])+"' "
    res=db.select(qry)
    return render_template("ship/view rating.html",data=res)






 #%%%%%%%%%*******************!!!!!!!!!!!!!!!!!!!!staff----------$$$$$$$$$$$$$########################################################################



@app.route("/staff_home_page")
def staff_home_page():
    db=Db()
    return render_template("staff/staff home.html")



@app.route("/staff_view_profile")
def staff_view_profile():
    db=Db()
    qry="SELECT staff.*,ship.ship_name FROM staff INNER JOIN ship ON staff.ship_id=ship.ship_id WHERE `staff`.`login_id`='"+str(session['lid'])+"'"
    # qry="SELECT * FROM `staff` WHERE `login_id`='"+str(session['lid'])+"' "
    print(qry)

    res=db.selectOne(qry)

    return render_template("staff/view profile.html",data=res)








@app.route("/staff_view_work")
def staff_view_work():
    db=Db()
    qry="select * from work inner join `allocate work` on work.work_id=`allocate work`.work_id where staff_id='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template("staff/view work.html",data=res)


@app.route("/staff_update_work_status/<wid>")
def staff_update_work_status(wid):
    db=Db()
    qry="update work set status='completed' where work_id='"+wid+"' "
    res=db.update(qry)
    qry1="update `allocate work` set status='compleleted' where work_id='"+wid+"'"
    res1=db.update(qry1)
    return "ok"




@app.route("/staff_activities_in_work/<aid>")
def staff_activities_in_work(aid):
    db=Db()
    qry="select * from  work  where work_id='"+aid+"'"
    res=db.selectOne(qry)
    print(res)
    return render_template("staff/activities in work.html",data=res)




@app.route("/staff_activities_in_work_post",methods=['post'])
def staff_activities_in_work_post():
    id=request.form['aid']
    date=request.form['textfield']
    status=request.form['textfield2']
    activities=request.form['textfield3']
    db=Db()
    qry="insert into `activities in work` (work_id,staff_id,date,status,activities) VALUE ('"+id+"','"+str(session['lid'])+"','"+date+"','"+status+"','"+activities+"')"
    res=db.insert(qry)
    return "ok"



@app.route("/staff_view_activities_in_work")
def staff_view_activities_in_work():
    db=Db()
    qry="select `activities in work`.date as dt ,`activities in work`.*,work.* from `activities in work` inner join work on work.work_id=`activities in work`.work_id where staff_id='"+str(session['lid'])+"' "
    res=db.select(qry)
    return render_template("staff/view activities in work.html",data=res)




















#======================================ANDROID===============================




@app.route("/userreg",methods=['post'])
def userreg():
    name=request.form["name"]
    place=request.form["place"]
    post=request.form["post"]
    pin=request.form["pin"]
    phone=request.form["phone"]
    email=request.form["email"]
    gender=request.form["gender"]
    image=request.form["image"]
    password=request.form["password"]
    db=Db()
    qry="INSERT INTO login VALUES('','"+email+"','"+password+"','user') "
    res=db.insert(qry)
    qry1="INSERT INTO USER VALUES('','"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+phone+"','"+email+"','"+gender+"','"+image+"')"
    db.insert(qry1)
    return jsonify(status="ok")



@app.route('/user_login',methods=['post'])
def user_login():
    username=request.form['username']
    password=request.form['password']

    db=Db()
    qry = "SELECT * FROM login WHERE username = '" + username + "' AND PASSWORD = '" + password + "'"
    res = db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid=res['login_id'],type="user")
    else:
        return jsonify(status="no")



@app.route('/user_view_profile',methods=['post'])
def user_view_profile():
    tid=request.form['tid']
    db=Db()
    qry="SELECT * FROM USER WHERE login_id='"+str(tid)+"' "
    res=db.selectOne(qry)
    return jsonify(status='ok',name = res['name'],place=res['place'],post=res['post'],pin=res['pin'],phone=res['phone'],email=res['email'],gender=res['gender'],image=res['image'])






@app.route('/user_view_ship',methods=['post'])
def user_view_ship():

    db=Db()
    qry="SELECT * FROM ship  "
    data=db.select(qry)
    return jsonify(status="ok",data=data)





@app.route('/user_send_complaint',methods=['post'])
def user_send_complaint():
    db=Db()
    ul_id=request.form['ul_id']
    complaint=request.form['complaint']

    db=Db()
    qry="INSERT INTO complaint(`date`,`ul_id`,`complaint`,`status`) VALUES(CURDATE(),'"+ul_id+"','"+complaint+"','pending')"
    res = db.insert(qry)
    return jsonify(status="ok")

@app.route('/user_sent_rating',methods=['post'])
def user_sent_rating():
    ship_id=request.form['ship_id']
    lid=request.form['lid']
    rating=request.form['rating']
    review=request.form['review']
    db=Db()
    qry="INSERT INTO rating (`user_id`,`ship_id`,`rating`,`review`,`date`) VALUES ('lid','ship_id','"+rating+"','"+review+"',CURDATE())"
    res=db.insert(qry)
    return jsonify(status="ok")



@app.route('/user_view_complaint',methods=['post'])
def user_view_complaint():
    db=Db()
    ul_id=request.form['ul_id']
    qry="select * from complaint where ul_id='"+ul_id+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/user_view_rating',methods=['post'])
def user_view_rating():
    db=Db()
    lid=request.form['lid']
    qry="select * from rating where lid='"+str(lid)+"' "
    res=db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/user_view_room',methods=['post'])
def user_view_room():
    db=Db()
    lid=request.form['ship_id']
    qry="select * from room where ship_id='"+str(lid)+"' "
    print(qry)
    res=db.select(qry)
    return jsonify(status="ok",data=res)








@app.route('/user_view_journey',methods=['post'])
def user_view_journey():
    db=Db()
    ship_id = request.form['ship_id']
    print(ship_id)
    qry="select * from journey where `ship_id`='"+ship_id+"' "
    print(qry)
    res=db.select(qry)
    return jsonify(status="ok",data=res)










@app.route('/user_view_facilities',methods=['post'])
def user_view_facilities():
    db=Db()

    ship_id=request.form['ship_id']
    # print(ship_id)
    qry= "select * from facilities WHERE ship_id='"+ship_id+"' "
    print(qry)

    res=db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/user_booking',methods=['post'])
def user_booking():
    db=Db()
    ship_id=request.form['ship_id']
    login_id=request.form['lid']
    no_user=request.form['no_user']
    qry="INSERT INTO booking (`ship_id`,`login_id`,`status`,`date`,`no_user`) VALUES ('"+ship_id+"','"+login_id+"','pending',CURDATE(),'"+no_user+"') "
    res=db.insert(qry)
    return jsonify(status="ok",data=res)


@app.route('/user_view_booking',methods=['post'])
def user_view_booking():
    db=Db()
    login_id=request.form['lid']
    qry="SELECT * FROM `booking` JOIN `ship` ON `booking`.`ship_id`=`ship`.`ship_id` JOIN `room` ON `room`.`ship_id`=`ship`.`ship_id` WHERE `booking`.`login_id`='"+login_id+"'"
    # qry="SELECT `booking`.*,`room`.*,`ship`.* FROM `booking` JOIN room ON `room`.`ship_id`=`booking`.`ship_id` JOIN `ship` ON `ship`.`login_id`=`room`.`ship_id` WHERE `booking`.`login_id`='"+login_id+"' "
    print(qry)
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/user_allocate_booking',methods=['post'])
def user_allocate_booking():
    room_id=request.form['room_id']
    user_id=request.form['user_id']
    ship_id=request.form['ship_id']
    qry = "INSERT INTO `allocate room` (room_id,user_id) VALUES ('" + room_id + "','" + user_id + "')"
    db = Db()
    db.insert(qry)
    res=db.insert(qry)

    qry1=" INSERT INTO booking (`ship_id`,`login_id`,`status`,`date`,`no_user`) VALUES('"+ship_id+"','"+user_id+"','pending',CURDATE(),'0')"
    res=db.insert(qry1)
    return jsonify(status="ok")




@app.route('/user_view_time',methods=['post'])
def user_view_time():
    db=Db()
    s_id=request.form['ship_id']
    qry = "SELECT * FROM schedule where ship_id='"+s_id+"'"
    res = db.select(qry)
    return jsonify(status="ok", data=res)


@app.route('/user_view_allocated_rooms')
def user_view_allocated_rooms():
    db=Db()


@app.route('/user_signup',methods=['post'])
def user_signup():
    db=Db()


    name = request.form['name']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    image = request.form['image']
    import time, datetime
    from encodings.base64_codec import base64_decode
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open("C:\\Users\\user\\PycharmProjects\\cruize in my hand\\static\\user\\" + timestr + ".jpg", "wb")
    path = "/static/user/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    password=request.form['password']
    qry = "INSERT INTO login VALUES('','" + email + "','" + password + "','user') "
    res = db.insert(qry)
    # qry1 = "INSERT INTO USER(name,place,post,pin,phone,email,gender,image) values ('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+phone+"','"+email+"','"+gender+"','"+path+"')"
    qry1="INSERT INTO `user`(login_id,`name`,`place`,`post`,`pin`,`phone`,`email`,`gender`,`image`) VALUES('"+str(res)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+phone+"','"+email+"','"+gender+"','"+path+"')"
    res1 = db.insert(qry1)
    return jsonify(status="ok")






if __name__ == '__main__':
    app.run(port=4000,debug=True,host='0.0.0.0')
