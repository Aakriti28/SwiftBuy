import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

// import { User } from '../user';
import {Notification} from './notification';
// import {Product} from '../_models/product';
// import {Login} from '../_models/login';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient, private cookieService: CookieService) { }

    getNotifications() {
        console.log('getNotifications');
        // let headers = new Headers({
        //     'Content-Type': 'application/json',
        //     'X-CSRFToken': this.getCookie('csrftoken')
        // });
        // let options = new RequestOptions({ headers: headers, withCredentials: true });
        // return this.http.get('http://localhost:8080/api/users/' + userid + '/notifications');
        return this.http.get<Notification[]>(`http://localhost:8000/notifications`, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
    }

    // getcatalog() {
    //     console.log('getcatalog');
    //     return this.http.get<Product[]>(`http://192.168.0.104:8000/home/catalog`);
    // }

    // getProduct(productid: number) {
    //     console.log('getProduct productid: ' + productid);
    //     return this.http.get<Product>(`http://192.168.0.104:8000/home/catalog/products/${productid}`);

    // }

    // getCart() {
    //     console.log('getCart');
    //     return this.http.get<Product[]>('http://192.168.0.104:8000/home/cart');
    // }

    // getPlaceOrder(paymentid: number) {
    //     return this.http.post(`http://192.168.0.104:8000/home/order`, (paymentid));
    // }

    // register(user: User) {
    //     console.log('register user: ' + JSON.stringify(user));
    //     return this.http.post('http://192.168.0.104:8000/signup/', (user));
    // }

    // login(user: Login) {
    //     console.log('Login user: ' + JSON.stringify(user));
    //     return this.http.post('http://192.168.0.104:8000/login/', (user));
    // }

    // delete(id: number) {
    //     return this.http.delete(`${config.apiUrl}/users/${id}`);
    // }
}