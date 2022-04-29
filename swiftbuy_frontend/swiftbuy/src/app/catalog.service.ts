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

  // private headers = new Headers({'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'});
  // getCatalog(): Observable<any>{
  //   return this.http.get(this._catalogUrl,{ headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}, withCredentials: true });
  // }
  getCatalog(): Observable<any>{
    return this.http.get(this._catalogUrl,{ headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
    // return this.http.get(this._catalogUrl,{ observe:'response', withCredentials: true });
    

  }

  getCatalogProducts(categoryid: number): Observable<any> {
    console.log('getCatalogProducts');
    return this.http.get(`http://localhost:8000/catalog/${categoryid}`, { headers: { 'Content-Type': 'application/json','X-CSRFToken': this.cookieService.get('csrftoken')  }, withCredentials: true });
  }
}