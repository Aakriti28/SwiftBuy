import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CatalogService {
  private _catalogUrl = 'http://localhost:8000/catalog';
  constructor(private http: HttpClient) { }

  getCatalog(): Observable<any>{
    return this.http.get(this._catalogUrl);
  }
}
