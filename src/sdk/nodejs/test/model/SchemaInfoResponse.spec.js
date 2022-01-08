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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SelfManagedOsdu);
  }
}(this, function(expect, SelfManagedOsdu) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('SchemaInfoResponse', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.SchemaInfoResponse();
      });

      it('should create an instance of SchemaInfoResponse', function() {
        // TODO: update the code to test SchemaInfoResponse
        expect(instance).to.be.a(SelfManagedOsdu.SchemaInfoResponse);
      });

      it('should have the property schemaInfos (base name: "schemaInfos")', function() {
        // TODO: update the code to test the property schemaInfos
        expect(instance).to.have.property('schemaInfos');
        // expect(instance.schemaInfos).to.be(expectedValueLiteral);
      });

      it('should have the property offset (base name: "offset")', function() {
        // TODO: update the code to test the property offset
        expect(instance).to.have.property('offset');
        // expect(instance.offset).to.be(expectedValueLiteral);
      });

      it('should have the property count (base name: "count")', function() {
        // TODO: update the code to test the property count
        expect(instance).to.have.property('count');
        // expect(instance.count).to.be(expectedValueLiteral);
      });

      it('should have the property totalCount (base name: "totalCount")', function() {
        // TODO: update the code to test the property totalCount
        expect(instance).to.have.property('totalCount');
        // expect(instance.totalCount).to.be(expectedValueLiteral);
      });

    });
  });

}));
