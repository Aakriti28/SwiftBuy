import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class SellerService {
  private _historyUrl = 'http://localhost:8000/sellinfo/history';
  constructor(private http: HttpClient, private cookieService: CookieService) { }

  getSellHistory(): Observable<any>{
    return this.http.get(this._historyUrl,{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }
}
