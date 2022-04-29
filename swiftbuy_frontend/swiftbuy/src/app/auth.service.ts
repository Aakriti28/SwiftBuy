import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Registration_info } from './registration_details';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _registerUrl = 'http://localhost:8000/signup';
  private _loginUrl = 'http://localhost:8000/login';
  private _logoutUrl = 'http://localhost:8000/logout';
  constructor(private http: HttpClient,  private cookieService: CookieService) { }

  registerUser(new_user: Registration_info): Observable<any>{
    return this.http.post(this._registerUrl, new_user, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }

  loginUser(user: any): Observable<any>{
    return this.http.post(this._loginUrl, user, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }

  logoutUser(): Observable<any>{
    return this.http.post(this._logoutUrl, {}, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }
}
