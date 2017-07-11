# -*- coding: utf-8 -*-
﻿from __future__ import absolute_import,unicode_literals
def get_data():
	"""เป็นคำสั่งดึงชื่อประเทศในโลก รูปแบบภาษาไทย
	คืนค่า list
	"""
	return [u'อัฟกานิสถาน', u'แอลเบเนีย', u'แอลจีเรีย', u'อเมริกันซามัว', u'อันดอร์รา', u'แองโกลา', u'แองกวิลลา', u'ออสเตรเลียนแอนตาร์กติกเทร์ริทอรี', u'แอนติกาและบาร์บูดา', u'อาร์เจนตินา', u'อาร์มีเนีย', u'อารูบา', u'ออสเตรเลีย', u'ออสเตรีย', u'อาเซอร์ไบจาน','บาฮามาส', u'บาห์เรน', u'บังกลาเทศ', u'บาร์เบโดส', u'เบลารุส', u'เบลเยียม', u'เบลีซ', u'เบนิน', u'เบอร์มิวดา', u'ภูฏาน', u'โบลิเวีย', u'บอสเนียและเฮอร์เซโกวีนา', u'บอตสวานาa', u'เกาะบูเวต (Bouvetøya)', u'บราซิล', u'บริติชอินเดียนโอเชียนเทร์ริทอรี', u'หมู่เกาะบริติชเวอร์จิน', u'บรูไนดารุสซาลาม', u'บัลแกเรีย', u'บูร์กินาฟาโซ', u'บุรุนดี', u'กัมพูชา', u'แคเมอรูน', u'แคนาดา', u'กาบูเวร์ดี', u'หมู่เกาะเคย์แมน', u'สาธารณรัฐแอฟริกากลาง', u'ชาด', u'ชิลี', u'จีน', u'เกาะคริสต์มาส', u'หมู่เกาะโคโคส (คีลิง)', u'โคลอมเบีย', u'คอโมโรส', u'สาธารณรัฐคองโก', u'หมู่เกาะคุก', u'คอสตาริกา', u'โกตดิวัวร์ (ไอวอรีโคสต์)', u'โครเอเชีย', u'คิวบา', u'ไซปรัส', u'สาธารณรัฐเช็ก','เดนมาร์ก', u'จิบูตี', u'ดอมินีกา', u'สาธารณรัฐโดมินิกัน','เอกวาดอร์', u'อียิปต์', u'เอลซัลวาดอร์', u'อิเควทอเรียลกินี', u'เอริเทรีย', u'เอสโตเนีย', u'เอธิโอเปีย','หมู่เกาะแฟโร', u'หมู่เกาะฟอล์กแลนด์', u'ฟิจิ', u'ฟินแลนด์', u'ฝรั่งเศส', u'เฟรนช์เกียนา', u'เฟรนช์โปลินีเซีย', u'เฟรนช์เซาเทิร์นและแอนตาร์กติกแลนส์','กาบอง', u'แกมเบีย', u'จอร์เจีย', u'เยอรมนี', u'กานา', u'ยิบรอลตาร์', u'กรีซ', u'กรีนแลนด์', u'เกรเนดา', u'กัวเดอลุป', u'กวม', u'กัวเตมาลา', u'เกิร์นซีย์', u'กินี', u'กินี-บิสเซา', u'กายอานา','เฮติ', u'เกาะเฮิร์ดและหมู่เกาะแมกดอนัลด์', u'นครรัฐวาติกัน', u'ฮอนดูรัส', u'ฮ่องกง', u'ฮังการี','ไอซ์แลนด์', u'อินเดีย', u'อินโดนีเซีย', u'อิหร่าน', u'อิรัก', u'ไอร์แลนด์', u'เกาะแมน', u'อิสราเอล', u'อิตาลี','จาเมกา', u'ญี่ปุ่น', u'เจอร์ซีย์', u'จอร์แดน','คาซัคสถาน', u'เคนยา', u'คิริบาส', u'เกาหลีใต้', u'เกาหลีเหนือ', u'คูเวต', u'คีร์กีซสถาน','ลาว', u'ลัตเวีย', u'เลบานอน', u'เลโซโท', u'ไลบีเรีย', u'ลิเบีย', u'ลิกเตนสไตน์', u'ลิทัวเนีย', u'ลักเซมเบิร์ก','มาเก๊า', u'สาธารณรัฐมาซิโดเนีย', u'มาดากัสการ์', u'มาลาวี', u'มาเลเซีย', u'มัลดีฟส์', u'มาลี', u'มอลตา', u'หมู่เกาะมาร์แชลล์', u'มาร์ตีนิก', u'มอริเตเนีย', u'มอริเชียส', u'มายอต', u'เม็กซิโก', u'ไมโครนีเซีย', u'มอลโดวา', u'โมนาโก', u'มองโกเลีย', u'มอนเตเนโกร', u'มอนต์เซอร์รัต', u'โมร็อกโก', u'โมซัมบิก', u'พม่า', u'นามิเบีย', u'นาอูรู', u'เนปาล', u'เนเธอร์แลนด์แอนทิลลีส', u'เนเธอร์แลนด์', u'นิวแคลิโดเนีย', u'นิวซีแลนด์', u'นิการากัว', u'ไนเจอร์', u'ไนจีเรีย', u'นีอูเอ', u'เกาะนอร์ฟอล์ก', u'หมู่เกาะนอร์เทิร์นมาเรียนา', u'นอร์เวย์', u'โอมาน', u'ปากีสถาน', u'ปาเลา', u'รัฐปาเลสไตน์', u'ปานามา', u'ปาปัวนิวกินี', u'ปารากวัย', u'เปรู', u'ฟิลิปปินส์', u'หมู่เกาะพิตแคร์น', u'โปแลนด์', u'โปรตุเกส', u'เปอร์โตริโก','กาตาร์','เรอูว์นียง', u'โรมาเนีย', u'รัสเซีย', u'รวันดา','แซ็ง-บาร์เตเลมี', u'เซนต์เฮเลนา', u'เซนต์คิตส์และเนวิส', u'เซนต์ลูเซีย', u'แซ็ง-มาร์แต็ง', u'แซงปีแยร์และมีเกอลง', u'เซนต์วินเซนต์และเกรนาดีนส์', u'ซามัว', u'ซานมารีโน', u'เซาตูเมและปรินซิปี', u'ซาอุดีอาระเบีย', u'เซเนกัล', u'เซอร์เบีย', u'เซเชลส์', u'เซียร์ราลีโอน', u'สิงคโปร์', u'สโลวาเกีย', u'สโลวีเนีย', u'หมู่เกาะโซโลมอน', u'โซมาเลีย', u'แอฟริกาใต้', u'เกาะเซาท์จอร์เจียและหมู่เกาะเซาท์แซนด์วิช', u'สเปน', u'ศรีลังกา', u'ซูดาน', u'ซูรินาม', u'สฟาลบาร์', u'ยานไมเอน', u'สวาซิแลนด์', u'สวีเดน', u'สวิตเซอร์แลนด์', u'ซีเรีย','ไต้หวัน', u'ทาจิกิสถาน', u'แทนซาเนีย', u'ไทย', u'ติมอร์-เลสเต', u'โตโก', u'โตเกเลา', u'ตองกา', u'ตรินิแดดและโตเบโก', u'ตูนิเซีย', u'ตุรกี', u'เติร์กเมนิสถาน', u'หมู่เกาะเติกส์และหมู่เกาะเคคอส', u'ตูวาลู','ยูกันดา', u'ยูเครน', u'สหรัฐอาหรับเอมิเรตส์', u'สหราชอาณาจักร', u'สหรัฐอเมริกา', u'เกาะเล็กรอบนอกของสหรัฐอเมริกา', u'หมู่เกาะเวอร์จินของสหรัฐอเมริกา', u'อุรุกวัย', u'อุซเบกิสถาน','วานูอาตู', u'เวเนซุเอลา', u'เวียดนาม','วาลลิสและฟุตูนา', u'เวสเทิร์นสะฮารา','เยเมน', u'แซมเบีย', u'ซิมบับเว']