# REBL
# An API demo

REBL is an ongoing concept as an eccommerce + creative outlet web app I made for my friends. Recently I decided to revisit this old project and build an api on top of it.
## DEMO

I hosted the app on heroku @https://infinite-hamlet-35050.herokuapp.com so you don't have to fork my repo. Instead,
add the the path /shopapi/v1/ or shopapi/v2/ to access api root.

![image](https://user-images.githubusercontent.com/41171387/51468887-ff99f080-1d3d-11e9-9146-7b549163a22c.png)

for the sake of this demo, I will only show how to access endpoints for all products. click on the products GUI link or currentpath/products/
![image](https://user-images.githubusercontent.com/41171387/51469213-dc237580-1d3e-11e9-8348-deae7fc6865f.png)

I have integrated multiple search for you to play with. Field filters will provide all products greater than or equal to the integer you've inputed. Precondtions for the field filter search are stock must be left blank or an integer .The search bar queries with respect to the products name and description field. You can see how implemented these filters in shopapi/views.py.
![image](https://user-images.githubusercontent.com/41171387/51469608-b9de2780-1d3f-11e9-90ed-3368e5aedf21.png)

Finally, you can add, delete and fake purchase on the main shop url
https://infinite-hamlet-35050.herokuapp.com/shop/ and add delete items to the cart. You can also 'fake pay' with the integrated stripe api if you use the fake credit card #: 4242 424242424242, cvc:123, MM/yy: any date in the future. Unfortunately, you will not get a thank you mail in your inbox since I am still using the sandbox host with mailgun.
![image](https://user-images.githubusercontent.com/41171387/51471755-93bb8600-1d45-11e9-896c-8ec22c2d63ce.png)

![image](https://user-images.githubusercontent.com/41171387/51471769-9ae29400-1d45-11e9-80e8-3048df895083.png)




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
