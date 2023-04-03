# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:27:43 2023

@author: Administrator
"""

# coding=gbk
import psycopg2

# 连接数据库
conn = psycopg2.connect(database='postgres',user='postgres',password='0217',host='localhost',port='5432');
print('连接成功')

# 建立游标
cur = conn.cursor()
cur.execute('''--建立表
create table public.v6_time_pref_pts_utf_wgs84_py(
   	gid SERIAL8 PRIMARY KEY NOT NULL,
   	name_py VARCHAR(254),
   	name_ch VARCHAR(254),
   	name_ft VARCHAR(254),
   	x_coor float8,
   	y_coor float8,
   	pres_loc VARCHAR(60),
   	type_py VARCHAR(15),
   	type_ch VARCHAR(15),
   	lev_rank VARCHAR(1),
   	beg_yr int8,
   	beg_rule VARCHAR(1),
   	end_yr int8,
   	end_rule VARCHAR(1),
   	note_id int8,
   	obj_type VARCHAR(7),
   	sys_id int8,
   	geo_src VARCHAR(10),
   	compiler VARCHAR(15),
   	gecomplr VARCHAR(10),
   	checker VARCHAR(10),
   	ent_date VARCHAR(15),
   	beg_chg_ty VARCHAR(30),
   	end_chg_ty VARCHAR(30),
   	geom geometry);

-- 建立索引
CREATE INDEX v6_time_pref_pts_utf_wgs84_py_index ON v6_time_pref_pts_utf_wgs84_py USING btree(gid);
-- 表说明
COMMENT ON TABLE public.v6_time_pref_pts_utf_wgs84_py IS '第6版中国历史地理时间序列点数据';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.gid IS '主键ID';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.name_py IS '拼音名称';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.name_ch IS '简体中文名称';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.name_ft IS '繁体中文名称';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.x_coor IS '经度';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.y_coor IS '纬度';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.pres_loc IS '现所在地';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.type_py IS '建制类型拼音';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.type_ch IS '建制类型简体中文';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.lev_rank IS '建制等级';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.beg_yr IS '建制开始时间';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.beg_rule IS '开始时间精度';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.end_yr IS '建制结束时间';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.end_rule IS '结束时间精度';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.note_id IS '系统id';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.obj_type IS 'geometry对象类型';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.sys_id IS '系统id';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.geo_src IS 'geometry数据来源';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.compiler IS '编辑人员';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.gecomplr IS '绘制人员';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.checker IS '审核人员';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.ent_date IS '结束时间';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.beg_chg_ty IS '建制开始原因';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.end_chg_ty IS '建制结束原因';
COMMENT ON COLUMN public.v6_time_pref_pts_utf_wgs84_py.geom IS 'geometry对象';''')

f=open(r'D:\HTML_Project\map_data\v6_time_pref_pts_utf_wgs84.txt','r',encoding='utf-8')

# 按行读入text
flines = f.readlines()
for line in flines:
    # 去掉干扰，切词
    abbrlist=line.replace("'","").split('\t')
    
    # 具体属性名 
    # name_py,name_ch,name_ft,x_coor,y_coor,pres_loc,type_py,type_ch,lev_rank,beg_yr,beg_rule,end_yr,end_rule,note_id,obj_type,sys_id,geo_src,compiler,gecomplr,checker,ent_date,beg_chg_ty,end_chg_ty,geom
    name_py='null'
    if(abbrlist[0]!=''):
        name_py="'"+abbrlist[0]+"'"
        
    name_ch='null'
    if (abbrlist[1]!=''):
        name_ch="'"+abbrlist[1]+"'"
        
    name_ft='null'
    if (abbrlist[2]!=''):
        name_ft="'"+abbrlist[2]+"'"
        
    x_coor='null'
    if (abbrlist[3]!=''):
        x_coor=abbrlist[3]

    y_coor='null'
    if (abbrlist[4]!=''):
        y_coor=abbrlist[4]
        
    pres_loc='null'
    if (abbrlist[5]!=''):
        pres_loc="'"+abbrlist[5]+"'"

    type_py='null'
    if (abbrlist[6]!=''):
        type_py="'"+abbrlist[6]+"'"

    type_ch='null'
    if (abbrlist[7]!=''):
        type_ch="'"+abbrlist[7]+"'"

    lev_rank='null'
    if (abbrlist[8]!=''):
        lev_rank="'"+abbrlist[8]+"'"

    beg_yr='null'
    if (abbrlist[9]!=''):
        beg_yr=abbrlist[9]

    beg_rule='null'
    if (abbrlist[10]!=''):
        beg_rule="'"+abbrlist[10]+"'"

    end_yr='null'
    if (abbrlist[11]!=''):
        end_yr=abbrlist[11]

    end_rule='null'
    if (abbrlist[12]!=''):
        end_rule="'"+abbrlist[12]+"'"

    note_id='null'
    if (abbrlist[13]!=''):
        note_id=abbrlist[13]

    obj_type='null'
    if (abbrlist[14]!=''):
        obj_type="'"+abbrlist[14]+"'"

    sys_id='null'
    if (abbrlist[15]!=''):
        sys_id=abbrlist[15]

    geo_src='null'
    if (abbrlist[16]!=''):
        geo_src="'"+abbrlist[16]+"'"

    compiler='null'
    if (abbrlist[17]!=''):
        compiler="'"+abbrlist[17]+"'"

    gecomplr='null'
    if (abbrlist[18]!=''):
        gecomplr="'"+abbrlist[18]+"'"

    checker='null'
    if (abbrlist[19]!=''):
        checker="'"+abbrlist[19]+"'"

    ent_date='null'
    if (abbrlist[20]!=''):
        ent_date="'"+abbrlist[20]+"'"

    beg_chg_ty='null'
    if (abbrlist[21]!=''):
        beg_chg_ty="'"+abbrlist[21]+"'"

    end_chg_ty='null'
    if (abbrlist[22]!=''):
        end_chg_ty="'"+abbrlist[22]+"'"

    geom='null'
    if (abbrlist[23]!=''):
        geom="st_geomfromtext('"+abbrlist[23]+"',4326)"
        
        
    sqltxt="INSERT INTO v6_time_pref_pts_utf_wgs84_py(" \
    \
        "name_py,name_ch,name_ft,x_coor,y_coor,pres_loc,type_py,type_ch,lev_rank,beg_yr,beg_rule," \
    \
        "end_yr,end_rule,note_id,obj_type,sys_id,geo_src,compiler,gecomplr,checker,ent_date," \
    \
        "beg_chg_ty,end_chg_ty,geom) VALUES("+name_py+","+name_ch+","+name_ft+","+x_coor+","+y_coor+"," \
    \
        +pres_loc+","+type_py+","+type_ch+","+lev_rank+","+beg_yr+","+beg_rule+","+end_yr+","+end_rule+","\
    \
        +note_id+","+obj_type+","+sys_id+","+geo_src+","+compiler+","+gecomplr+","+checker+","+ent_date+","\
    \
        +beg_chg_ty+","+end_chg_ty+","+geom+")"

    print(sqltxt)
    
    # 执行SQL
    cur.execute(sqltxt)

# 关闭连接
conn.commit()
conn.close()
print('插入完成')
