/** @odoo-module **/
import { registry } from '@web/core/registry';
import { Component } from '@odoo/owl';
export class HelloAction extends Component {
    setup() {
        console.log("Hello, Odoo action executed!");
    }        
};

// Specify the template to use (must match the XML t-name)
HelloAction.template = "hello_odoo.HelloTemplate";

// Register the JS action
registry.category("actions").add("action_print_message", HelloAction)
