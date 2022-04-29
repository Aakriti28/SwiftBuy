import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class CatalogService {
  private _catalogUrl = 'http://localhost:8000/catalog';
  constructor(private http: HttpClient, private cookieService: CookieService) { }

  getCatalog(): Observable<any>{
    return this.http.get(this._catalogUrl,{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }
}