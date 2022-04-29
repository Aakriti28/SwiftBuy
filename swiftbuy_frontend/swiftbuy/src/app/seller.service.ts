import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { Product_info } from './product_details';

@Injectable({
  providedIn: 'root'
})
export class SellerService {
  private _historyUrl = 'http://localhost:8000/sellinfo/history';
  constructor(private http: HttpClient, private cookieService: CookieService) { }

  getSellHistory(): Observable<any>{
    return this.http.get(this._historyUrl,{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }

  addProduct(product: Product_info){
    return this.http.post('http://localhost:8000/sellinfo/addproduct',product,{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }

  getSellerProduct(){
    return this.http.get('http://localhost:8000/sellinfo/selling',{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }
}
