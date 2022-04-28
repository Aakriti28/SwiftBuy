import { Component, OnInit } from '@angular/core';
import { CatalogService } from '../catalog.service';\

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {
  catalog_list: any = {};
  constructor(private service: CatalogService) { }

  ngOnInit(): void {
    this.getCatalogFromAPI()
  }

  getCatalogFromAPI(){
    this.service.getCatalog().subscribe(
      response => {
        this.catalog_list = response;
        console.log(this.catalog_list)
      },
      error => {
        console.log("error in getcatalogFromAPI : ",error)
      }
    )
  }

}
