-- Disable the foreign key to be able to insert and update rows
-- SET GLOBAL FOREIGN_KEY_CHECKS=1;
-- SHOW GLOBAL VARIABLES LIKE 'FOREIGN_KEY_CHECKS'; 

-- select * from matchas



INSERT INTO matchas( id, matcha_name, matcha_qty,item_qty, 
matcha_short_description, taste_description,taste_notes, price, img, 
small_img_one,small_img_two, small_img_three, small_img_four,
created_at, updated_at, user_id, bag_id)

VALUES(3, "Sayaka", "100g", 1, "Rich & Smooth", "Our recommendation for people new to our matcha, Sayaka is a more light-hearted, smooth tea in the rich category. Its sweetness and umami are accompanied by a hint of bitterness.
",
"We recommend Sayaka for your first taste of Ippodo matcha, as it is a smooth blend with umami and just a hint of astringency. 
Try this matcha as koicha to experience the full depth and nuances of its character. As usucha, Sayaka is an accessible tea to serve to beginners and connoisseurs alike at teatime. For matcha lattes, we usually recommend a medium-to-light category matcha with more astringency, but some will choose Sayaka for its bright color, umami, and soft astringency.",
75, "item_imgs/sayaka_small_imgs/Sayaka_big_img.webp", "item_imgs/sayaka_small_imgs/Sayaka_big_img.webp",
"item_imgs/sayaka_small_imgs/sayaka_small2.webp", "item_imgs/sayaka_small_imgs/sayaka_small3.webp", "item_imgs/sayaka_small_imgs/Sayaka100g-plate_1024x1.webp",
NOW(), NOW(), 1,1)