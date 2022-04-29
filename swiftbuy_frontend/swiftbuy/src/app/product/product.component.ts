import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {

  product = [] as any

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.getProduct();
  }

  private getProduct() {
    this.userService.getProduct(1)
      .pipe(first())
      .subscribe(data => this.product = data);
  }

}
