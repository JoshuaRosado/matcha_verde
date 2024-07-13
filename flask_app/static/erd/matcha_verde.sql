
INSERT INTO matchas( id, matcha_name, matcha_qty,item_qty, 
matcha_short_description, taste_description,taste_notes, price, img, 
small_img_one,small_img_two, small_img_three, small_img_four,
created_at, updated_at, user_id, bag_id)

VALUES(1, "Ummon", "40g", 1, "Rich & Robust", 
"Ummon has a powerful umami, deep emerald green color, and sweet aroma. This matcha is a treat to be savored.",
"For decades Ummon has been one of the richest, most full-forced matcha blends in our selection. Our blending and tasting team members have shared their personal tasting comments on this tea below.",
30, "matcha_verde_website/flask_app/static/imgs/matcha_types_imgs/ippodo-tea-ummon-40g-matcha_98cfdb6b-463f-472e-aced-416ce61f7405_750x750.png",
"matcha_verde_website/flask_app/static/imgs/item_imgs/ummon_small_imgs/ummon_small1.avif", "matcha_verde_website/flask_app/static/imgs/item_imgs/ummon_small_imgs/ummon_small2.webp",
"matcha_verde_website/flask_app/static/imgs/item_imgs/ummon_small_imgs/ummon_small3.webp", NULL, 
NOW(), NOW(),1,1)