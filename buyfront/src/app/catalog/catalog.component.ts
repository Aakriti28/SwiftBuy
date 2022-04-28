import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { Product } from '../_models/product';
import { UserService } from '../_services/user.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {

  products = [] as any




  constructor(private userService: UserService) {

   }

  ngOnInit(): void {
    this.loadAllProducts();
  }

    private loadAllProducts() {
      this.userService.getcatalog()
          .pipe(first())
          .subscribe(data => this.products = data);
  }
}






