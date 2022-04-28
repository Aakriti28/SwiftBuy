import { Component, OnInit } from '@angular/core';
import { CatalogService } from '../catalog.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-catalog-products',
  templateUrl: './catalog-products.component.html',
  styleUrls: ['./catalog-products.component.scss']
})
export class CatalogProductsComponent implements OnInit {

  private sub: any = {};
  id: number;
  constructor(private route: ActivatedRoute, private service: CatalogService) { 
    this.id=1;
  }

  ngOnInit(): void {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id']; // (+) converts string 'id' to a number
   });
   this.getCatalogProducts();
  }

  getCatalogProducts(){
    
  }

}
