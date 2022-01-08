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
    describe('FileLegal', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.FileLegal();
      });

      it('should create an instance of FileLegal', function() {
        // TODO: update the code to test FileLegal
        expect(instance).to.be.a(SelfManagedOsdu.FileLegal);
      });

      it('should have the property legaltags (base name: "legaltags")', function() {
        // TODO: update the code to test the property legaltags
        expect(instance).to.have.property('legaltags');
        // expect(instance.legaltags).to.be(expectedValueLiteral);
      });

      it('should have the property otherRelevantDataCountries (base name: "otherRelevantDataCountries")', function() {
        // TODO: update the code to test the property otherRelevantDataCountries
        expect(instance).to.have.property('otherRelevantDataCountries');
        // expect(instance.otherRelevantDataCountries).to.be(expectedValueLiteral);
      });

      it('should have the property status (base name: "status")', function() {
        // TODO: update the code to test the property status
        expect(instance).to.have.property('status');
        // expect(instance.status).to.be(expectedValueLiteral);
      });

    });
  });

}));
