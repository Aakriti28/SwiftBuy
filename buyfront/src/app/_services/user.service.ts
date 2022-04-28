import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { User } from '../_models/user';
import {Notification} from '../_models/notification';
import {Product} from '../_models/product';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { }

    getNotifications() {
        console.log('getNotifications');
        // return this.http.get('http://localhost:8080/api/users/' + userid + '/notifications');
        return this.http.get<Notification[]>(`http://192.168.0.104:8000/notifications`);
    }

    getcatalog() {
        console.log('getcatalog');
        return this.http.get<Product[]>(`http://192.168.0.104:8000/home/catalog`);
    }

    getProduct(productid: number) {
        console.log('getProduct productid: ' + productid);
        return this.http.get<Product>(`http://192.168.0.104:8000/home/catalog/products/${productid}`);

    }

    getCart() {
        console.log('getCart');
        return this.http.get<Product[]>('http://192.168.0.104:8000/home/cart');
    }

    getPlaceOrder(paymentid: number) {
        return this.http.post(`http://192.168.0.104:8000/home/order`, (paymentid));
    }

    register(user: User) {
        console.log('register user: ' + JSON.stringify(user));
        return this.http.post('http://192.168.0.104:8000/signup/', (user));
    }

    // delete(id: number) {
    //     return this.http.delete(`${config.apiUrl}/users/${id}`);
    // }
}