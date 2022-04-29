import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient, private cookieService: CookieService) { }

    getNotifications(): Observable<any> {
        console.log('getNotifications');
        return this.http.get(`http://127.0.0.1:8000/notifications`, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
    }

    // getProduct(productid: number) {
    //     console.log('getProduct productid: ' + productid);
    //     return this.http.get<Product>(`http://192.168.0.104:8000/home/catalog/products/${productid}`);

    // }

    getCart(): Observable<any> {
        console.log('getCart');
        return this.http.get(`http://localhost:8000/cart`, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
    }

    placeOrder(paymentid: number): Observable<any> {
        return this.http.post(`http://localhost:8000/order`, (paymentid), { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
    }

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