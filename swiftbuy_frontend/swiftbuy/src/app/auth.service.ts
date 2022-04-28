import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Registration_info } from './registration_details';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _registerUrl = 'http://localhost:8000/signup';
  private _loginUrl = 'http://localhost:8000/login';
  constructor(private http: HttpClient) { }

  registerUser(new_user: Registration_info): Observable<any>{
    return this.http.post(this._registerUrl, new_user);
  }

  loginUser(user: any): Observable<any>{
    return this.http.post(this._loginUrl, user);
  }
}
