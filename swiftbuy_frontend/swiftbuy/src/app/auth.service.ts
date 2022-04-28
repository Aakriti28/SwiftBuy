import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Registration_info } from './registration_details';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _registerUrl = 'http://localhost:3000/api/register';
  private _loginUrl = 'http://localhost:3000/api/login';
  constructor(private http: HttpClient) { }

  registerUser(new_user: Registration_info): Observable<any>{
    return this.http.post(this._registerUrl, new_user);
  }

  loginUser(user: any): Observable<any>{
    return this.http.post(this._loginUrl, user);
  }
}
