/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/RegisterFilter'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./RegisterFilter'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.RegisterCreateAction = factory(root.SelfManagedOsdu.ApiClient, root.SelfManagedOsdu.RegisterFilter);
  }
}(this, function(ApiClient, RegisterFilter) {
  'use strict';

  /**
   * The RegisterCreateAction model module.
   * @module model/RegisterCreateAction
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>RegisterCreateAction</code>.
   * @alias module:model/RegisterCreateAction
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>RegisterCreateAction</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/RegisterCreateAction} obj Optional instance to populate.
   * @return {module:model/RegisterCreateAction} The populated <code>RegisterCreateAction</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'String');
      if (data.hasOwnProperty('name'))
        obj.name = ApiClient.convertToType(data['name'], 'String');
      if (data.hasOwnProperty('description'))
        obj.description = ApiClient.convertToType(data['description'], 'String');
      if (data.hasOwnProperty('contactEmail'))
        obj.contactEmail = ApiClient.convertToType(data['contactEmail'], 'String');
      if (data.hasOwnProperty('img'))
        obj.img = ApiClient.convertToType(data['img'], 'String');
      if (data.hasOwnProperty('url'))
        obj.url = ApiClient.convertToType(data['url'], 'String');
      if (data.hasOwnProperty('filter'))
        obj.filter = RegisterFilter.constructFromObject(data['filter']);
    }
    return obj;
  }

  /**
   * @member {String} id
   */
  exports.prototype.id = undefined;

  /**
   * @member {String} name
   */
  exports.prototype.name = undefined;

  /**
   * @member {String} description
   */
  exports.prototype.description = undefined;

  /**
   * @member {String} contactEmail
   */
  exports.prototype.contactEmail = undefined;

  /**
   * Reference link to an image file that can be usd in an UI to represent the action.
   * @member {String} img
   */
  exports.prototype.img = undefined;

  /**
   * @member {String} url
   */
  exports.prototype.url = undefined;

  /**
   * @member {module:model/RegisterFilter} filter
   */
  exports.prototype.filter = undefined;


  return exports;

}));
